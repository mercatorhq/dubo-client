import os
import json

import sqlite3
import time
from typing import Dict, List, Optional, Type
import urllib.parse

import pandas as pd
import altair as alt
from pydeck.io.html import deck_to_html

from dubo.config import (
    BASE_API_URL,
    CATEGORIZE_CHART_API_URL,
    CHART_API_URL,
    get_dubo_key,
    query_endpoint,
    api_key,
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


def http_GET(url: str, params: dict | None = None, headers: dict | None = None) -> dict:
    if params:
        url += "?" + _encode_params(params)
    try:
        from js import XMLHttpRequest  # type: ignore

        req = XMLHttpRequest.new()
        req.open("GET", url, False)

        # Set additional headers if provided
        if headers:
            for key, value in headers.items():
                req.setRequestHeader(key, value)

        req.send(None)  # No body for GET request
        return json.loads(req.responseText)
    except ImportError:
        from urllib.request import Request, urlopen as urllib_open_url

        # Create a Request object to allow setting headers
        req = Request(url, method="GET")

        # Set additional headers if provided
        if headers:
            for key, value in headers.items():
                req.add_header(key, value)

        # Use as a GET
        return json.loads(urllib_open_url(req).read())


def http_POST(
    url: str, *, body: dict, params: dict | None = None, headers: dict | None = None
) -> dict:
    if params:
        url += "?" + _encode_params(params)
    try:
        from js import XMLHttpRequest, Blob  # type: ignore

        req = XMLHttpRequest.new()
        req.open("POST", url, False)

        # Set default content type header
        req.setRequestHeader("Content-Type", "application/json")

        # Set additional headers if provided
        if headers:
            for key, value in headers.items():
                req.setRequestHeader(key, value)

        blob = Blob.new([json.dumps(body)], {type: "application/json"})
        req.send(blob)
        return json.loads(req.responseText)
    except ImportError:
        from urllib.request import Request, urlopen

        req = Request(url, data=json.dumps(body).encode("utf-8"), method="POST")

        # Set default headers
        req.add_header("Content-Type", "application/json")
        req.add_header("x-dubo-lib", "python")

        # Set additional headers if provided
        if headers:
            for key, value in headers.items():
                req.add_header(key, value)

        res = urlopen(req).read()
        return json.loads(res)


class DuboException(Exception):
    pass


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
            "api_key": api_key,
            "descriptions": column_descriptions,
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
        raise DuboException(e)


def chart(
    query: str,
    df: pd.DataFrame,
    specify_chart_type: str | None = None,
    verbose=False,
    **kwargs,
):
    chart_type: str | None = specify_chart_type
    if not chart_type:
        chart_type = http_GET(
            CATEGORIZE_CHART_API_URL,
            params={
                "text_input": query,
            },
        )
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
    res = http_POST(
        BASE_API_URL + "/query/dispatch",
        body={
            "user_query": query,
            "fast": fast,
        },
        headers={"x-dubo-key": api_key},
    )
    return res["id"]


def retrieve_result(tracking_id: str) -> dict:
    """
    Poll for the result using the provided tracking_id.
    """
    delay = 0.1
    max_delay = 10  # max delay, adjust as needed
    while True:
        res = http_GET(
            BASE_API_URL + "/query/result",
            params={
                "id": tracking_id,
            },
            headers={"x-dubo-key": api_key},
        )
        if res["status"] == "success":
            return res["result"]
        elif res["status"] == "failed":
            raise DuboException(res["error"])
        else:
            time.sleep(delay)
            delay = min(delay * 2, max_delay)


def dispatch_and_retrieve(query: str, fast: bool = False) -> dict:
    """
    Convenience function to dispatch the query and retrieve the result.
    """
    tracking_id = dispatch_query(query, fast)
    return retrieve_result(tracking_id)


def query(
    payload: str,
    fast: bool = False,
) -> DataResult:
    if get_dubo_key() is None:
        raise DuboException(
            "You must set the DUBO_API_KEY environment variable to use "
            "this function."
        )
    res = dispatch_and_retrieve(payload, fast)
    return DataResult(
        id=res["id"],
        query_text=res["query_text"],
        status=res["status"],
        results_set=res["results_set"],
        row_count=res["row_count"],
    )
