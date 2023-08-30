from .ask_dubo import (
    ask,
    chart,
    create_doc,
    delete_doc,
    generate_sql,
    get_all_docs,
    get_doc,
    query,
    search_tables,
    update_doc,
)  # noqa
from .config import DOCS_URL, FEEDBACK_URL
from .__version__ import *  # noqa


MSG = f"Dubo | Examples: {DOCS_URL} | Discord: {FEEDBACK_URL} | Privacy policy: https://mercator.tech/privacy"

print(MSG)
