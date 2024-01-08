import json
import os
from http import HTTPStatus
from uuid import UUID
import sqlglot

import sqlite3
from typing import Dict, List, Optional, Type
import warnings

import pandas as pd
import altair as alt
from pydeck.io.html import deck_to_html

from dubo.common import DuboException
from dubo.config import BASE_API_URL, get_dubo_key
from dubo.entities import DataResult
from dubo.query_utils import dispatch_and_retrieve

from dubo.api_client import AuthenticatedClient
from dubo.api_client.api.dubo import (
    read_query_v1_dubo_query_get,
)

from dubo.api_client.api.enterprise import (
    ask_dispatch_api_v1_dubo_query_generate_post,
    create_documentation_api_v1_dubo_documentation_post,
    delete_document_by_id_api_v1_dubo_documentation_delete,
    filter_documentation_endpoint_api_v1_dubo_query_filter_documentation_get,
    read_all_api_v1_dubo_documentation_get,
    read_one_api_v1_dubo_documentation_data_source_documentation_id_get,
    update_document_api_v1_dubo_documentation_put,
)
from dubo.api_client.api.sdk import (
    create_dubo_chart_v1_dubo_chart_post,
    get_query_execution_category_v1_dubo_categorize_chart_get,
)
from dubo.api_client.models import *
from dubo.api_client.types import *
from dubo.api_client.models.matched_doc import MatchedDoc


api_key = get_dubo_key()
client = AuthenticatedClient(
    base_url=BASE_API_URL,
    token=api_key,
    auth_header_name="x-dubo-key",
    prefix="",
)


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

    if not possible_query:
        raise DuboException(f"Unable to produce a result for the query: {query}")
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
    chart_type: ChartType | None = None,
    verbose=False,
    **kwargs,
):
    """
    Ask Dubo to generate a chart.

    :param query: The chart to ask Dubo to generate.
    :param df: The DataFrame for the chart.
    :param chart_type: Type of chart: ChartType.DECK_GL or ChartType.VEGA_LITE.
    :param verbose: Whether to print verbose logs.
    :type query: str
    :type df: pd.DataFrame
    :type chart_type: ChartType | None
    :type verbose: bool
    :return: The chart.

    ##### Example
    ```python
    import pandas as pd

    from dubo import chart
    from dubo.api_client.models import ChartType

    housing_df = pd.read_csv("https://raw.githubusercontent.com/ajduberstein/geo_datasets/master/housing.csv")

    chart(
        query="Map the houses",
        df=housing_df,
        chart_type=ChartType.DECK_GL,
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
    if not chart_type:
        chart_type_str = get_query_execution_category_v1_dubo_categorize_chart_get.sync(
            client=client,
            text_input=query,
        )
        chart_type = ChartType(str(chart_type_str).lower())
    else:
        chart_type = ChartType(str(chart_type))
    if ChartType(chart_type) not in (
        ChartType.VEGA_LITE,
        ChartType.DECK_GL,
    ):
        raise ValueError(
            f"Chart type must be one of: VEGA_LITE, DECK_GL, got {chart_type}"
        )

    if verbose:
        print("Generating a chart of type:", chart_type)

    data_snippet = df.head().to_dict(orient="records")
    data_snippet = [
        DuboChartQueryDataSnippetItem.from_dict(item) for item in data_snippet
    ]

    res = create_dubo_chart_v1_dubo_chart_post.sync_detailed(
        client=client,
        json_body=DuboChartQuery(
            user_query=query,
            data_snippet=data_snippet,
            fast=False,
            chart_type=chart_type,
        ),
    )
    if res.status_code != HTTPStatus.OK:
        raise DuboException(
            f"Failed to call API, status code: {res.status_code}, content: {res.content.decode('utf-8')}"
        )
    chart = res.parsed

    if chart_type == ChartType.VEGA_LITE:
        if len(df) > 10000:
            warnings.warn("Input has more than 10,000 rows. Only the first 10,000 will be used.", UserWarning)
        chart["data"] = {"values": df.head(10000).to_dict(orient="records")}
        chart["height"] = kwargs.get("height") or 390
        chart["width"] = kwargs.get("width") or 500
        return alt.Chart.from_dict(chart, **kwargs)

    if chart_type == ChartType.DECK_GL:
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
    query_text: str,
    fast: bool = False,
) -> DataResult:
    """
    Ask Dubo a question.

    :param query_text: The question to ask Dubo.
    :param fast: Use faster, less accurate model
    :type query_text: str
    :type fast: bool
    :return: The SQL query.

    ##### Example
    ```python
    from dubo import query

    query("How many area types are there?")

    # DataResult(
    #  id='query-56513883-6749-4f2b-ad57-7bb8cb350161',
    #  query_text='How many area types are there?',
    #  status=QueryStatus.SUCCESS,
    #  results_set=[{'count': 9}],
    #  row_count=1
    # )
    ```
    """

    return dispatch_and_retrieve(client, query_text, fast)


def generate_sql(
    query_text: str,
    fast: bool = False,
    pretty: bool = True,
) -> str:
    """
    Ask Dubo to generate a SQL query.

    :param query_text: The plain text query.
    :param fast: Use faster, less accurate model
    :type query_text: str
    :type fast: bool
    :return: The SQL query.

    ##### Example
    ```python
    from dubo import query

    query("How many area types are there?")

    # "SELECT COUNT(DISTINCT type) AS num_area_types FROM public.area"
    ```
    """

    body = CreateApiQuery(
        query_text=query_text,
        fast=fast,
        mode=CreateApiQueryMode.JUST_SQL_TEXT,
    )
    res = ask_dispatch_api_v1_dubo_query_generate_post.sync_detailed(
        client=client,
        json_body=body,
    )
    if res.status_code != 200:
        raise DuboException(
            f"Failed to dispatch query, status code: {res.status_code}, content: {res.content.decode('utf-8')}"
        )
    res = res.parsed

    if not res:
        raise DuboException("Failed to generate SQL.")
    if pretty and res.sql_text:
        return sqlglot.parse_one(res.sql_text).sql(pretty=True)
    return res.sql_text


def search_tables(
    query_text: str,
    fast: bool = False,
) -> List[AttenuatedDDL]:
    """
    Ask Dubo to return the list of tables that are a potential match for this query.

    :param query_text: The plain text query.
    :param fast: Use faster, less accurate model
    :type query_text: str
    :type fast: bool
    :return: The list of tables.

    ##### Example
    ```python
    from dubo import query

    query("How many area types are there?")

    # [
    #   AttenuatedDDL(
    #      cols=[
    #          TableColumn(column_name='name', data_type='character varying', is_nullable=False, table_name='area_type', schema_name='public', is_partitioning_column=None),
    #          TableColumn(column_name='parent', data_type='integer', is_nullable=True, table_name='area_type', schema_name='public', is_partitioning_column=None),
    #          TableColumn(column_name='description', data_type='text', is_nullable=True, table_name='area_type', schema_name='public', is_partitioning_column=None),
    #          TableColumn(column_name='gid', data_type='uuid', is_nullable=False, table_name='area_type', schema_name='public', is_partitioning_column=None),
    #          TableColumn(column_name='id', data_type='integer', is_nullable=False, table_name='area_type', schema_name='public', is_partitioning_column=None),
    #          TableColumn(column_name='child_order', data_type='integer', is_nullable=False, table_name='area_type', schema_name='public', is_partitioning_column=None),
    #      ],
    #      table_name='area_type',
    #      schema_name='public',
    #      id='e3e10474-aa55-4654-bfb8-6592dc540127',
    #      database_name='postgres',
    #      description='Table storing different types of areas, including their parent-child relationships and descriptions',
    #   ),
    #  ...
    # ]
    ```
    """
    body = CreateApiQuery(
        query_text=query_text,
        fast=fast,
        mode=CreateApiQueryMode.JUST_TABLES,
    )
    res = ask_dispatch_api_v1_dubo_query_generate_post.sync_detailed(
        client=client,
        json_body=body,
    )
    if res.status_code != 200:
        raise DuboException(
            f"Failed to dispatch query, status code: {res.status_code}, content: {res.content.decode('utf-8')}"
        )
    res = res.parsed

    return res.tables


def filter_documentation(
    user_query: str,
    data_source_documentation_id: Optional[str] = None,
    page_number: int = 1,
    page_size: int = 25,
) -> List[MatchedDoc]:
    """
    Search in documentation

    :param user_query: The search query.
    :param data_source_documentation_id: The documentation id.
    :param page_number: The page number.
    :param page_size: The page size.
    :type user_query: str
    :type data_source_documentation_id: str, optional
    :type page_number: int, optional
    :type page_size: int, optional
    :return: The list of results (paginated): body, score and matched_doc_id (datasource id)

    ##### Example
    ```python
    from dubo import filter_documentation

    res = filter_documentation(
        user_query="describe the area type table",
        data_source_documentation_id="c1d62c33-4561-4b5f-b2c2-e0203cee1f7b",
        page_number=1,
        page_size=10,
    )
    # [ MatchedDoc(
    #    body='The area_type table contains the list of area types',
    #    score=0.947,
    #    matched_doc_id='2be09019-8d48-49a0-aeb0-4837a57e444c'
    #  ), ...]
    ```
    """

    res = filter_documentation_endpoint_api_v1_dubo_query_filter_documentation_get.sync_detailed(
        client=client,
        user_query=user_query,
        data_source_documentation_id=data_source_documentation_id,
        page_number=page_number,
        page_size=page_size,
    )
    if res.status_code != HTTPStatus.OK:
        raise DuboException(
            f"Failed to call API, status code: {res.status_code}, content: {res.content.decode('utf-8')}"
        )

    return res.parsed.data


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
    from dubo import create_doc

    create_doc(
        file_path="./documentation.txt",
        shingle_length=1000,
        step=500,
    )

    # DataSourceDocument(
    #   id='c1d62c33-4561-4b5f-b2c2-e0203cee1f7b',
    #   file_name='documentation.txt',
    #   data_source_id=...,
    #   organization_id=...,
    #   created_at=...,
    #   updated_at=...,
    # )
    ```
    """

    with open(file_path, "rb") as doc:
        file_name = os.path.basename(file_path)
        file = File(
            payload=doc,
            file_name=file_name,
        )

        body = BodyCreateDocumentationApiV1DuboDocumentationPost(file)

        res = create_documentation_api_v1_dubo_documentation_post.sync_detailed(
            client=client,
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
    from dubo import get_doc

    get_doc("c1d62c33-4561-4b5f-b2c2-e0203cee1f7b")

    # DataSourceDocument(
    #   id='c1d62c33-4561-4b5f-b2c2-e0203cee1f7b',
    #   file_name='documentation.txt',
    #   data_source_id=...,
    #   organization_id=...,
    #   created_at=...,
    #   updated_at=...,
    # )
    ```
    """
    res = read_one_api_v1_dubo_documentation_data_source_documentation_id_get.sync_detailed(
        client=client,
        data_source_documentation_id=data_source_documentation_id,
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

    get_all_docs()

    # [{'file_name': 'documentation.txt', 'id': 'c1d62c33-4561-4b5f-b2c2-e0203cee1f7b'}]
    ```
    """
    res = read_all_api_v1_dubo_documentation_get.sync_detailed(
        client=client,
    )
    if res.status_code != HTTPStatus.OK:
        raise DuboException(
            f"Failed to call API, status code: {res.status_code}, content: {res.content.decode('utf-8')}"
        )
    res = res.parsed

    if res is None:
        return []

    return [{"file_name": doc.file_name, "id": doc.id} for doc in res]


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

    # True
    ```
    """

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

    # True
    ```
    """
    # No need to fetch by name, just use the provided ID directly.

    res = delete_document_by_id_api_v1_dubo_documentation_delete.sync_detailed(
        client=client,
        data_source_documentation_id=data_source_documentation_id,
    )
    if res.status_code != HTTPStatus.OK:
        raise DuboException(
            f"Failed to call API, status code: {res.status_code}, content: {res.content.decode('utf-8')}"
        )

    return res.parsed
