"""Check if the config file exists, if not, create it."""

import os

from dubo import __version__  # noqa

QUERY_API_URL = "https://api.dubo.gg/v1/dubo/query"
CHART_API_URL = "https://api.dubo.gg/v1/dubo/chart"
BASE_API_URL = os.getenv("DUBO_BASE_URL") or "https://api.dubo.gg/api/v1/dubo"
CATEGORIZE_CHART_API_URL = "https://api.dubo.gg/v1/dubo/categorize-chart"
DOCS_URL = "https://dubo.gg/"
FEEDBACK_URL = "https://discord.gg/Cw7rfpkD"

query_endpoint = os.environ.get("DUBO_QUERY_URL", QUERY_API_URL)
_api_key = os.environ.get("DUBO_API_KEY", None)


def set_dubo_key(key: str):
    """
    Set the API key.
    """
    global _api_key
    _api_key = key


def get_dubo_key():
    """
    Get the API key.
    """
    return _api_key
