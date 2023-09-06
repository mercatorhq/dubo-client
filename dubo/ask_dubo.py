import json
import os
import sqlite3
import time
from uuid import UUID
import urllib.parse
from typing import Any, Dict, List, Optional, Type, Union

import requests
import pandas as pd
import altair as alt
from pydeck.io.html import deck_to_html

from dubo.common import DuboException
from dubo.config import (
    BASE_API_URL,
    CATEGORIZE_CHART_API_URL,
    CHART_API_URL,
    get_dubo_key,
    query_endpoint,
)
from dubo.entities import DataResult


def _encode_params(params: dict) -> str:
    # URL-encode a dict into a query string and append it to the URL
    # if the value is a list, then create multiple entries for the same key
    url_parts = ""
    for k, v in params.items():
        if v is None:
            continue
        if isinstance(v, list):
            for item in v:
                url_parts += f"{k}={urllib.parse.quote(str(item))}&"
        else:
            url_parts += f"{k}={urllib.parse.quote(str(v))}&"
    return url_parts[:-1]


def http_GET(
    url: str,
    params: dict[str, str] | None = None,
    headers: dict[str, str] | None = None,
) -> dict:
    if params:
        url += "?" + _encode_params(params)
    try:
        from js import XMLHttpRequest  # type: ignore

        req = XMLHttpRequest.new()
        req.open("GET", url, False)

        if headers:
            for key, value in headers.items():
                req.setRequestHeader(key, value)

        req.send(None)
        return json.loads(req.responseText)
    except (ImportError, ModuleNotFoundError):
        pass
    from urllib.request import Request, urlopen, HTTPError

    req = Request(url, method="GET")
    if headers:
        for key, value in headers.items():
            req.add_header(key, value)
    try:
        res = urlopen(
            req,
        )
        if res.status != 200:
            raise DuboException(res.error)
        text = res.read()
        return json.loads(text)
    except HTTPError as e:
        # If the server returns an error page, print its contents
        if e.fp:
            error_message = e.fp.read().decode("utf-8")
            raise Exception(f"Details: {error_message}")

    return json.loads(urlopen(req).read())


def http_POST(
    url: str, *, body: dict, params: dict | None = None, headers: dict | None = None
) -> dict:
    if params:
        url += "?" + _encode_params(params)
    try:
        from js import XMLHttpRequest, Blob  # type: ignore

        req = XMLHttpRequest.new()
        req.open("POST", url, False)
        req.setRequestHeader("Content-Type", "application/json")

        if headers:
            for key, value in headers.items():
                req.setRequestHeader(key, value)

        blob = Blob.new([json.dumps(body)], {type: "application/json"})
        res = req.send(blob)
        text = req.responseText
        if req.status != 200:
            raise DuboException(text)
        return json.loads(text)
    except (ImportError, ModuleNotFoundError):
        pass
    from urllib.request import Request, urlopen, HTTPError

    req = Request(url, data=json.dumps(body).encode("utf-8"), method="POST")

    req.add_header("Content-Type", "application/json")
    req.add_header("x-dubo-lib", "python")

    if headers:
        for key, value in headers.items():
            req.add_header(key, value)

    data_payload = json.dumps(body).encode("utf-8")
    try:
        res = urlopen(
            req,
            data=data_payload,
        )
        if res.status != 200:
            raise DuboException(res.error)
        text = res.read()
        return json.loads(text)
    except HTTPError as e:
        # If the server returns an error page, print its contents
        if e.fp:
            error_message = e.fp.read().decode("utf-8")
            raise Exception(f"Details: {error_message}")


def http_POST_with_file(
    url: str,
    *,
    file: Any,
    params: dict | None = None,
    headers: dict | None = None,
    data: dict | None = None,
) -> Union[dict, str]:
    if headers is None:
        headers = {}
    headers["x-dubo-lib"] = "python"

    try:
        files = {"file": file}
        res = requests.post(url, headers=headers, params=params, files=files, data=data)

        # Check for successful status code
        if res.status_code != 200:
            raise DuboException(res.content.decode("utf-8"))

        # Check Content-Type and process response accordingly
        if "application/json" in res.headers.get("Content-Type", ""):
            return res.json()
        else:
            return res.text  # Assuming that the UUID would be plain text
    except requests.RequestException as e:
        raise DuboException(str(e))


def http_DELETE(
    url: str,
    params: Optional[Dict[str, str]] = None,
    headers: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    api_key = get_dubo_key()

    if headers is None:
        headers = {}

    headers["x-dubo-key"] = api_key

    response = requests.delete(url, params=params, headers=headers)

    if response.status_code != 200:
        error_message = f"Failed to delete: {response.text}"
        try:
            error_details = response.json()
            error_message += f"\nDetails: {error_details}"
        except json.JSONDecodeError:
            pass

        raise DuboException(error_message)

    return response.json()


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
    possible_query = http_GET(
        query_endpoint,
        params={
            "user_query": query,
            "schemas": schemas,
            "api_key": get_dubo_key() or "",
            "descriptions": column_descriptions,  # type: ignore
        },
    )
    try:
        result = possible_query["query_text"]
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
    specify_chart_type: str | None = None,
    verbose=False,
    **kwargs,
):
    chart_type: str | None = specify_chart_type
    if not chart_type:
        params = {
            "text_input": query,
        }
        chart_type = http_GET(
            CATEGORIZE_CHART_API_URL,
            params=params,
        )  # type: ignore
    if chart_type not in ("VEGA_LITE", "DECK_GL"):
        raise ValueError("Chart type must be one of: VEGA_LITE, DECK_GL")

    if verbose:
        print("Generating a chart of type:", chart_type)

    charts = http_POST(
        CHART_API_URL,
        body={
            "user_query": query,
            "data_snippet": df.head().to_dict(orient="records"),
            "fast": False,
            "chart_type": chart_type.lower(),
        },
    )

    if chart_type == "VEGA_LITE":
        chart = charts[0]
        chart["data"] = {"values": df.sample(10000).to_dict(orient="records")}
        chart["height"] = kwargs.get("height") or 390
        chart["width"] = kwargs.get("width") or 500
        return alt.Chart.from_dict(chart, **kwargs)

    if chart_type == "DECK_GL":
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
    res = http_POST(
        BASE_API_URL + "/query/generate",
        body={
            "query_text": query,
            "fast": fast,
        },
        params={
            "x_dubo_key": api_key,
        },
        headers={"x-dubo-key": api_key},
    )
    return res["id"]


def retrieve_result(tracking_id: str) -> DataResult:
    """
    Poll for the result using the provided tracking_id.
    """
    delay = 0.1
    max_delay = 10
    api_key = get_dubo_key()
    while True:
        res = http_GET(
            BASE_API_URL + "/query/retrieve",
            params={
                "dispatch_id": tracking_id,
                "x_dubo_key": api_key,
            },
            headers={"x-dubo-key": api_key},
        )
        if res["status"] == "success":
            return DataResult(
                id=res["id"],
                query_text=res["query_text"],
                status=res["status"],
                results_set=res["results_set"],
                row_count=res["row_count"],
            )
        elif res["status"] == "failed":
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
    res = http_POST(
        BASE_API_URL + "/query/generate",
        body={
            "query_text": payload,
            "fast": fast,
            "mode": "just_sql_text",
        },
        params={"x_dubo_key": api_key, "mode": "just_sql_text"},
        headers={"x-dubo-key": api_key},
    )
    return res["sql_text"]


def search_tables(
    payload: str,
    fast: bool = False,
) -> List[dict]:
    api_key = get_dubo_key()
    res = http_POST(
        BASE_API_URL + "/query/generate",
        body={
            "query_text": payload,
            "fast": fast,
            "mode": "just_tables",
        },
        params={
            "x_dubo_key": api_key,
        },
        headers={"x-dubo-key": api_key},
    )
    return res["tables"]


def filter_documentation(
    user_query: str,
    data_source_documentation_id: Optional[str] = None,
    page_number: int = 1,
    page_size: int = 25,
) -> List[dict]:
    api_key = get_dubo_key()
    params = {
        "user_query": user_query,
        "page_number": page_number,
        "page_size": page_size,
        "x_dubo_key": api_key,
    }

    if data_source_documentation_id:
        params["data_source_documentation_id"] = data_source_documentation_id

    headers = {"x-dubo-key": api_key}

    res = http_GET(
        BASE_API_URL + "/query/filter-documentation", params=params, headers=headers
    )

    return res["data"]


def create_doc(
    file: Any,
    shingle_length: int = 1000,
    step: int = 500,
) -> Optional[UUID]:
    api_key = get_dubo_key()

    res = http_POST_with_file(
        BASE_API_URL + "/documentation",
        file=file,
        headers={"x-dubo-key": api_key},
        data={
            "shingle_length": shingle_length,
            "step": step,
        },
    )

    return res


def get_doc(data_source_documentation_id: str) -> dict:
    api_key = get_dubo_key()

    url = f"{BASE_API_URL}/documentation"

    res = http_GET(
        url,
        headers={"x-dubo-key": api_key},
        params={"data_source_documentation_id": data_source_documentation_id},
    )

    return res


def get_all_docs() -> List[Dict[str, str]]:
    api_key = get_dubo_key()

    url = f"{BASE_API_URL}/documentation"

    res = http_GET(
        url,
        headers={"x-dubo-key": api_key},
    )

    if res is not None:
        simplified_res = [
            {"file_name": doc["file_name"], "id": doc["id"]} for doc in res
        ]
        return simplified_res

    return []


def update_doc(
    data_source_documentation_id: str,
    file_path: str,
    shingle_length: int = 1000,
    step: int = 500,
) -> bool:
    api_key = get_dubo_key()

    url = f"{BASE_API_URL}/documentation"
    headers = {
        "x-dubo-key": api_key,
    }

    with open(file_path, "rb") as f:
        files = {"file": f}
        params = {
            "data_source_documentation_id": str(UUID(data_source_documentation_id)),
            "shingle_length": shingle_length,
            "step": step,
        }

        response = requests.put(url, headers=headers, files=files, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            raise DuboException(
                f"Documentation update failed with status code {response.status_code}: {response.text}"
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

    url = f"{BASE_API_URL}/documentation"
    headers = {"x-dubo-key": api_key}

    # Make sure to replace this line with actual implementation
    # if your http_DELETE function's signature is different.
    response = http_DELETE(
        url,
        headers=headers,
        params={"data_source_documentation_id": data_source_documentation_id},
    )

    if response is None:
        raise Exception(
            "Failed to delete document, no response received from the server."
        )

    return response
