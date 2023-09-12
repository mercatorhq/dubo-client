import json
import os
from http import HTTPStatus
from uuid import UUID

import sqlite3
import time
from typing import Any, Dict, List, Optional, Type

import pandas as pd
import altair as alt
from pydeck.io.html import deck_to_html
from dubo.common import DuboException

from dubo.config import BASE_API_URL, get_dubo_key
from dubo.entities import DataResult

from dubo.api_client import Client as DuboApiClient
from dubo.api_client.api.dubo import (
    read_query_v1_dubo_query_get,
)
from dubo.api_client.api.enterprise import (
    ask_dispatch_api_v1_dubo_query_generate_post,
    ask_poll_api_v1_dubo_query_retrieve_get,
    create_documentation_api_v1_dubo_documentation_post,
    delete_document_by_id_api_v1_dubo_documentation_delete,
    read_all_api_v1_dubo_documentation_get,
    read_one_api_v1_dubo_documentation_data_source_documentation_id_get,
    update_document_api_v1_dubo_documentation_put,
)
from dubo.api_client.api.sdk import (
    create_dubo_chart_v1_dubo_chart_post,
    get_query_execution_category_v1_dubo_categorize_chart_get
)
from dubo.api_client.models import *


client = DuboApiClient(base_url=BASE_API_URL)


def ask(
    query: str,
    data: List[pd.DataFrame] | pd.DataFrame,
    verbose: bool = True,
    rtype: Type = pd.DataFrame,
    column_descriptions: Optional[Dict[str, str]] = None,
) -> pd.DataFrame | List:
    """
    Ask Dubo a question about your data.

    :param query: The question to ask Dubo.
    :param data: The DataFrame to ask Dubo about.
    :param verbose: Whether to print the query that Dubo is running.
    :param column_descriptions: A dictionary of column names to descriptions.

    # Example
    ```python
    import pandas as pd
    from dubo import ask

    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    ask('What is the sum of a?', df)
    > [(6,)]
    ```
    :return The result of the query.
    :type query: str
    """
    conn = sqlite3.connect(":memory:")

    if isinstance(data, pd.DataFrame):
        data = [data]
    if not all([isinstance(d, pd.DataFrame) for d in data]):
        raise TypeError(
            "Input for data must be a pandas.DataFrame but saw type: %s" % type(data)
        )
    schemas = []
    for i, dset in enumerate(data):
        tbl_name = f"tbl_{i}"
        dset.infer_objects().to_sql(tbl_name, conn, index=False)
        schema = conn.execute(
            f"SELECT sql FROM sqlite_schema WHERE name = '{tbl_name}'"
        ).fetchone()
        schemas.append(schema[0])
    possible_query = read_query_v1_dubo_query_get.sync(
        client=client,
        user_query=query,
        schemas=schemas,
        descriptions=column_descriptions,
        json_body=BodyReadQueryV1DuboQueryGet(),
    )
    try:
        result = possible_query.query_text
        if verbose:
            print(result)
    except KeyError:
        raise DuboException(f"Unable to produce a result for the query: {query}")
    try:
        if rtype == pd.DataFrame:
            return pd.read_sql(result, conn)
        elif rtype == list:
            return conn.execute(result).fetchall()
        else:
            raise TypeError(
                f"rtype must be either pd.DataFrame or list but saw type: {rtype}"
            )
    except Exception as e:
        raise DuboException(str(e))


def chart(
    query: str,
    df: pd.DataFrame,
    specify_chart_type: ChartType | None = None,
    verbose=False,
    **kwargs,
):
    chart_type: ChartType | None = specify_chart_type
    if not chart_type:
        chart_type = get_query_execution_category_v1_dubo_categorize_chart_get.sync(
            client=client,
            text_input=query,
        )
    if chart_type not in (ChartType.VEGA_LITE, ChartType.DECK_GL):
        raise ValueError("Chart type must be one of: VEGA_LITE, DECK_GL")

    if verbose:
        print("Generating a chart of type:", chart_type)

    data_snippet = df.head().to_dict(orient="records")
    data_snippet = list(map(lambda x: DuboChartQueryDataSnippetItem.from_dict(x), data_snippet))

    charts = create_dubo_chart_v1_dubo_chart_post.sync(
        client=client,
        json_body=DuboChartQuery(
            user_query=query,
            data_snippet=data_snippet,
            fast=False,
            chart_type=chart_type.lower()
        ),
    )

    if chart_type == ChartType.VEGA_LITE:
        chart = charts[0]
        chart["data"] = {"values": df.sample(10000).to_dict(orient="records")}
        chart["height"] = kwargs.get("height") or 390
        chart["width"] = kwargs.get("width") or 500
        return alt.Chart.from_dict(chart, **kwargs)

    if chart_type == ChartType.DECK_GL:
        chart = charts[0]
        for layer in chart["layers"]:
            if "data" in layer:
                layer["data"] = df.to_dict(orient="records")
        mapbox_key = (
            kwargs.pop("mapbox_key", None)
            or os.environ.get("MAPBOX_KEY")
            or ""  # noqa: E501
        )
        return deck_to_html(json.dumps(chart), mapbox_key=mapbox_key, **kwargs)

    raise ValueError(f"Unknown chart type: {chart_type}")


def dispatch_query(query: str, fast: bool = False) -> str:
    """
    Dispatch the query and get a tracking_id.
    """
    api_key = get_dubo_key()
    json_body = CreateApiQuery(
        query_text=query,
        fast=fast,
    )

    res = ask_dispatch_api_v1_dubo_query_generate_post.sync(
        client=client,
        x_dubo_key=api_key,
        json_body=json_body,
    )
    return res.id


def retrieve_result(tracking_id: str) -> DataResult:
    """
    Poll for the result using the provided tracking_id.
    """
    delay = 0.1
    max_delay = 10
    api_key = get_dubo_key()
    while True:
        res = ask_poll_api_v1_dubo_query_retrieve_get.sync(
            client=client,
            x_dubo_key=api_key,
            dispatch_id=tracking_id,
        )
        if res.status == QueryStatus.SUCCESS:
            return DataResult(
                id=res.id,
                query_text=res.query_text,
                status=res.status,
                results_set=list(map(lambda x: x.additional_properties, res.results_set)),
                row_count=res.row_count,
            )
        elif res.status == QueryStatus.FAILED:
            raise DuboException(res["error"])
        else:
            time.sleep(delay)
            delay = min(delay * 2, max_delay)


def dispatch_and_retrieve(query: str, fast: bool = False) -> DataResult:
    """
    Convenience function to generate the query and retrieve the result.
    """
    tracking_id = dispatch_query(query, fast)
    return retrieve_result(tracking_id)


def query(
    payload: str,
    fast: bool = False,
) -> DataResult:
    get_dubo_key()
    return dispatch_and_retrieve(payload, fast)


def generate_sql(
    payload: str,
    fast: bool = False,
) -> str:
    api_key = get_dubo_key()
    body = CreateApiQuery(
        query_text=payload,
        fast=fast,
        mode=CreateApiQueryMode.JUST_SQL_TEXT,
    )
    res = ask_dispatch_api_v1_dubo_query_generate_post.sync(
        client=client,
        x_dubo_key=api_key,
        json_body=body,
    )
    return res.sql_text


def search_tables(
    payload: str,
    fast: bool = False,
) -> List[AttenuatedDDL]:
    api_key = get_dubo_key()
    body = CreateApiQuery(
        query_text=payload,
        fast=fast,
        mode=CreateApiQueryMode.JUST_TABLES,
    )
    res = ask_dispatch_api_v1_dubo_query_generate_post.sync(
        client=client,
        x_dubo_key=api_key,
        json_body=body,
    )
    return res.tables


def create_doc(
    file: Any,
    shingle_length: int = 1000,
    step: int = 500,
) -> DataSourceDocument | HTTPValidationError:
    api_key = get_dubo_key()
    body = BodyCreateDocumentationApiV1DuboDocumentationPost(
        file=file,
    )

    res = create_documentation_api_v1_dubo_documentation_post.sync(
        client=client,
        x_dubo_key=api_key,
        multipart_data=body,
        shingle_length=shingle_length,
        step=step,
    )

    return res


def get_doc(data_source_documentation_id: str) -> DataSourceDocument | HTTPValidationError | None:
    api_key = get_dubo_key()
    return read_one_api_v1_dubo_documentation_data_source_documentation_id_get.sync(
        client=client,
        data_source_documentation_id=data_source_documentation_id,
        x_dubo_key=api_key,
    )


def get_all_docs() -> List[Dict[str, str]]:
    api_key = get_dubo_key()
    res = read_all_api_v1_dubo_documentation_get.sync(
        client=client,
        x_dubo_key=api_key,
    )

    if res is None:
        return []

    return [
        {"file_name": doc.file_name, "id": doc.id} for doc in res
    ]


def update_doc(
    data_source_documentation_id: str,
    file_path: str,
    shingle_length: int = 1000,
    step: int = 500,
) -> bool:
    api_key = get_dubo_key()

    with open(file_path, "rb") as file:
        body = BodyUpdateDocumentApiV1DuboDocumentationPut(
            file=file,
        )
        res = update_document_api_v1_dubo_documentation_put.sync_detailed(
            client=client,
            x_dubo_key=api_key,
            data_source_documentation_id=str(UUID(data_source_documentation_id)),
            shingle_length=shingle_length,
            step=step,
            multipart_data=body,
        )

        if res.status_code == HTTPStatus.OK:
            return True
        else:
            raise DuboException(
                f"Documentation update failed with status code {res.status_code}: {res.content.decode('utf-8')}"
            )


def delete_doc(data_source_documentation_id: str) -> bool:
    """
    Delete a document by its ID.

    Parameters:
        documentation_id (str): The ID of the document to delete.

    Returns:
        bool: True if the deletion was successful, False otherwise.
    """
    # No need to fetch by name, just use the provided ID directly.
    api_key = get_dubo_key()

    res = delete_document_by_id_api_v1_dubo_documentation_delete.sync(
        client=client,
        x_dubo_key=api_key,
        data_source_documentation_id=data_source_documentation_id,
    )

    return res
