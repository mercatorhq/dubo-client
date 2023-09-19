import json
import os
from http import HTTPStatus
from uuid import UUID

import sqlite3
from typing import Dict, List, Optional, Type

import pandas as pd
import altair as alt
from pydeck.io.html import deck_to_html

from dubo.common import DuboException
from dubo.config import BASE_API_URL, get_dubo_key
from dubo.entities import DataResult
from dubo.query_utils import dispatch_and_retrieve

from dubo.api_client import Client as DuboApiClient
from dubo.api_client.api.dubo import (
    read_query_v1_dubo_query_get,
)
from dubo.api_client.api.enterprise import (
    ask_dispatch_api_v1_dubo_query_generate_post,
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
from dubo.api_client.types import *


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
    :param rtype: Expected returned type.
    :param column_descriptions: A dictionary of column names to descriptions.
    :type query: str
    :type rtype: pd.DataFrame or list
    :return: The result of the query.

    ##### Example
    ```python
    import pandas as pd
    from dubo import ask

    data = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    ask('What is the sum of a?', data, rtype=list)

    # [(6,)]
    ```
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
    """
    Ask Dubo to generate a chart.

    :param query: The chart to ask Dubo to generate.
    :param df: The DataFrame for the chart.
    :param specify_chart_type: Type of chart: ChartType.DECK_GL or ChartType.VEGA_LITE.
    :param verbose: Whether to print verbose logs.
    :type query: str
    :type df: pd.DataFrame
    :type specify_chart_type: ChartType | None
    :type verbose: bool
    :return: The chart.

    ##### Example
    ```python
    import pandas as pd

    from dubo import chart
    from dubo.api_client.models import ChartType

    housing_df = pd.read_csv("https://raw.githubusercontent.com/ajduberstein/geo_datasets/master/housing.csv")

    res = chart(
        query="Map the houses",
        df=housing_df,
        specify_chart_type=ChartType.DECK_GL,
        as_string=True,
    )
    # <!DOCTYPE html>
    #    <html>
    #    ...
    #    <body>
    #        <div id="deck-container">
    #        </div>
    #    </body>
    #    <script>
    #        const container = document.getElementById('deck-container');
    #        ...
    ```
    """
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
    data_snippet = [
        DuboChartQueryDataSnippetItem.from_dict(item) for item in data_snippet
    ]

    charts = create_dubo_chart_v1_dubo_chart_post.sync(
        client=client,
        json_body=DuboChartQuery(
            user_query=query,
            data_snippet=data_snippet,
            fast=False,
            chart_type=chart_type,
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
    file_path: str,
    shingle_length: int = 1000,
    step: int = 500,
) -> DataSourceDocument:
    """
    Create Documentation.

    :param file_path: The path to the file to upload.
    :param shingle_length: TBC.
    :param step: TBC.
    :return: The documentation

    ##### Example
    ```python
    from dubo import update_doc

    update_doc(
        data_source_documentation_id=res.id,
        file_path="./documentation.txt",
        shingle_length=1000,
        step=500,
    )
    # > True

    res = create_doc(
        file_path="./documentation.txt",
        shingle_length=1000,
        step=500,
    )
    # > DataSourceDocument(
    #     id='c1d62c33-4561-4b5f-b2c2-e0203cee1f7b',
    #     file_name='documentation.txt',
    #     data_source_id=...,
    #     organization_id=...,
    #     created_at=...,
    #     updated_at=...,
    # )
    ```
    """
    api_key = get_dubo_key()

    with open(file_path, "rb") as doc:
        file_name = os.path.basename(file_path)
        file = File(
            payload=doc,
            file_name=file_name,
        )

        body = BodyCreateDocumentationApiV1DuboDocumentationPost(file)

        res = create_documentation_api_v1_dubo_documentation_post.sync_detailed(
            client=client,
            x_dubo_key=api_key,
            multipart_data=body,
            shingle_length=shingle_length,
            step=step,
        )

        if res.status_code == HTTPStatus.OK:
            return res.parsed
        else:
            raise DuboException(
                f"Documentation create failed with status code {res.status_code}: {res.content.decode('utf-8')}"
            )


def get_doc(data_source_documentation_id: str) -> DataSourceDocument:
    """
    Get one document by ID.

    :param data_source_documentation_id: The ID of the document to get.
    :return: The document

    ##### Example
    ```python
    from dubo import get_all_docs

    res = get_all_docs()
    # > DataSourceDocument(
    #     id='c1d62c33-4561-4b5f-b2c2-e0203cee1f7b',
    #     file_name='documentation.txt',
    #     data_source_id=...,
    #     organization_id=...,
    #     created_at=...,
    #     updated_at=...,
    # )
    ```
    """
    api_key = get_dubo_key()
    res = read_one_api_v1_dubo_documentation_data_source_documentation_id_get.sync_detailed(
        client=client,
        data_source_documentation_id=data_source_documentation_id,
        x_dubo_key=api_key,
    )

    if res.status_code == HTTPStatus.OK:
        return res.parsed
    else:
        raise DuboException(
            f"Documentation get failed with status code {res.status_code}: {res.content.decode('utf-8')}"
        )


def get_all_docs() -> List[Dict[str, str]]:
    """
    Get All Documents.

    :return: The list of documents (file_name and id)

    ##### Example
    ```python
    from dubo import get_all_docs

    res = get_all_docs()
    # > [{'file_name': 'documentation.txt', 'id': 'c1d62c33-4561-4b5f-b2c2-e0203cee1f7b'}]
    ```
    """
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
    """
    Update Document.

    :param data_source_documentation_id: The ID of the document to update.
    :param file_path: The path to the file to upload.
    :param shingle_length: TBC.
    :param step: TBC.
    :return: True if successful, False otherwise

    ##### Example
    ```python
    from dubo import update_doc

    update_doc(
        data_source_documentation_id="c1d62c33-4561-4b5f-b2c2-e0203cee1f7b",
        file_path="./documentation.txt",
        shingle_length=1000,
        step=500,
    )
    # > True
    ```
    """
    api_key = get_dubo_key()

    with open(file_path, "rb") as doc:
        file_name = os.path.basename(file_path)
        file = File(
            payload=doc,
            file_name=file_name,
        )
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

    :param data_source_documentation_id: The ID of the document to delete.
    :return: True if the deletion was successful, False otherwise

    ##### Example
    ```python
    from dubo import delete_doc

    delete_doc("c1d62c33-4561-4b5f-b2c2-e0203cee1f7b")
    # > True
    ```
    """
    # No need to fetch by name, just use the provided ID directly.
    api_key = get_dubo_key()

    res = delete_document_by_id_api_v1_dubo_documentation_delete.sync(
        client=client,
        x_dubo_key=api_key,
        data_source_documentation_id=data_source_documentation_id,
    )

    return res
