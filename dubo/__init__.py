from .ask_dubo import *  # noqa
from .config import DOCS_URL, FEEDBACK_URL


__title__ = "dubo"
__description__ = "Natural language analytics on any data frame or database."
__version__ = "0.2.12"


MSG = f"Dubo {__version__} | Examples: {DOCS_URL} | Contact: {FEEDBACK_URL} | Privacy policy: https://mercator.tech/privacy"

print(MSG)
