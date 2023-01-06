import json

import sqlite3
import urllib.parse

import pandas as pd

from dubo.config import query_endpoint, api_key


def _open_url(url: str, params: dict | None = None):
    if params:
        url += '?' + '&'.join([f'{k}={urllib.parse.quote_plus(v)}' for k, v in params.items() if v is not None])
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

def ask(query: str, data: pd.DataFrame, verbose: bool = False) -> pd.DataFrame:
    """
    Ask Dubo a question about your data.

    :param query: The question to ask Dubo.
    :param data: The DataFrame to ask Dubo about.
    :param verbose: Whether to print the query that Dubo is running.

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
    conn = sqlite3.connect(':memory:')
    if isinstance(data, pd.DataFrame):
        data.to_sql('tbl', conn, index=False)
    else:
        raise TypeError('Input for data must be a pandas DataFrame but saw type: %s' % type(data))
    schema = conn.execute("SELECT sql FROM sqlite_schema WHERE name = 'tbl'").fetchone()
    schema = schema[0]
    possible_query = _open_url(query_endpoint, params={'query': query, 'schema': schema, 'api_key': api_key})
    try:
        result = possible_query['query_text']
        if verbose:
            print(result)
    except KeyError:
        raise Exception("Unable to produce a result for the query: %s" % query)
    try:
        return pd.read_sql(result, conn)
    except Exception as e:
        raise DuboException(e)
