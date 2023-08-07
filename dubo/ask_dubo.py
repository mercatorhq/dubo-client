import json

import sqlite3
from typing import Dict, List, Optional, Type
import urllib.parse

import pandas as pd
import altair as alt
from pydeck.io.html import deck_to_html

from dubo.config import (
    CATEGORIZE_CHART_API_URL,
    CHART_API_URL,
    query_endpoint,
    api_key,
)  # noqa: E402


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


def http_GET(url: str, params: dict | None = None):
    if params:
        url += "?" + _encode_params(params)
    try:
        # Treat pyodide as a special case
        from pyodide.http import open_url as pyodide_open_url  # type: ignore

        return json.loads(pyodide_open_url(url).read())
    except ImportError:
        from urllib.request import urlopen as urlib_open_url

        # Use as a POST
        return json.loads(urlib_open_url(url).read())


def http_POST(url: str, *, body: dict, params: dict | None = None) -> dict:
    if params:
        url += "?" + _encode_params(params)
    try:
        from js import XMLHttpRequest, Blob  # type: ignore

        req = XMLHttpRequest.new()
        req.open("POST", url, False)
        blob = Blob.new([json.dumps(body)], {type: "application/json"})
        req.send(blob)
        return json.loads(req.responseText)
    except ImportError:
        from urllib.request import Request, urlopen

        req = Request(url, data=json.dumps(body).encode("utf-8"), method="POST")
        req.add_header("Content-Type", "application/json")
        req.add_header("x-dubo-lib", "python")
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
        chart["data"] = {"values": df.to_dict(orient="records")}
        return alt.Chart.from_dict(chart, **kwargs)

    if chart_type == "DECK_GL":
        chart = charts[0]
        for layer in chart["layers"]:
            if "data" in layer:
                layer["data"] = df.to_dict(orient="records")
        return deck_to_html(json.dumps(chart), **kwargs)

    raise ValueError(f"Unknown chart type: {chart_type}")
