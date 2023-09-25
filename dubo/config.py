"""Check if the config file exists, if not, create it."""

from dotenv import load_dotenv
import os

from dubo.common import DuboException

load_dotenv()
BASE_API_URL = os.getenv("DUBO_BASE_URL")

DOCS_URL = "https://dubo.gg/"
FEEDBACK_URL = "https://discord.gg/Cw7rfpkD"

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
    if not _api_key:
        raise DuboException(
            "You must set the DUBO_API_KEY environment variable to use "
            "this function."
        )
    return _api_key
