"""Check if the config file exists, if not, create it."""

import os

from dubo import __version__  # noqa

QUERY_API_URL = "https://api.dubo.gg/v1/dubo/query"
CHART_API_URL = "https://api.dubo.gg/v1/dubo/chart"
CATEGORIZE_CHART_API_URL = "https://api.dubo.gg/v1/dubo/categorize-chart"
DOCS_URL = "https://dubo.gg/"
FEEDBACK_URL = "https://discord.gg/Cw7rfpkD"

query_endpoint = os.environ.get("DUBO_QUERY_URL", QUERY_API_URL)
api_key = os.environ.get("DUBO_API_KEY", None)
