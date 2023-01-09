"""Check if the config file exists, if not, create it."""

import os

from dubo import __version__

API_URL = "https://dubo-api.mercator.tech/v1/dubo/query"
FEEDBACK_URL = "https://forms.gle/KvPm6niv9oUGRZhh8"
DOCS_URL = "https://dubo.mercator.tech/"

query_endpoint = os.environ.get("DUBO_QUERY_URL", API_URL)
api_key = os.environ.get("DUBO_API_KEY", None)
