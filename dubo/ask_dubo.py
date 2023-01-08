import json

import sqlite3
from typing import Dict, List, Optional
import urllib.parse

import pandas as pd

from dubo.config import query_endpoint, api_key


def _open_url(url: str, params: dict | None = None):
    if params:
        # URL-encode a dict into a query string and append it to the URL
        url += "?" + urllib.parse.urlencode(params)
    try:
        # Treat pyodide as a special case
        from pyodide.http import open_url as pyodide_open_url  # type: ignore

        return json.loads(pyodide_open_url(url).read())
    except ImportError:
        from urllib.request import urlopen as urlib_open_url

        # Use as a POST
        return json.loads(urlib_open_url(url).read())


class DuboException(Exception):
    pass


def ask(
    query: str,
    data: List[pd.DataFrame] | pd.DataFrame,
    verbose: bool = True,
    column_descriptions: Optional[Dict[str, str]] = None,
) -> pd.DataFrame:
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
            "Input for data must be a pandas DataFrame but saw type: %s" % type(data)
        )
    schemas = []
    for i, dset in enumerate(data):
        tbl_name = f"df{i}"
        dset.infer_objects().to_sql(tbl_name, conn, index=False)
        schema = conn.execute(
            f"SELECT sql FROM sqlite_schema WHERE name = '{tbl_name}'"
        ).fetchone()
        schemas.append(schema[0])
    possible_query = _open_url(
        query_endpoint,
        params={
            "query": query,
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
        raise DuboException("Unable to produce a result for the query: %s" % query)
    try:
        return pd.read_sql(result, conn)
    except Exception as e:
        raise DuboException(e)
