from .ask_dubo import (
    ask,
    chart,
    delete_documentation_by_name,
    generate_sql,
    get_all_documents_for_data_source,
    get_documentation_by_name,
    query,
    search_tables,
    update_documentation,
    upload_documentation,
)  # noqa
from .config import DOCS_URL, FEEDBACK_URL
from .__version__ import *  # noqa


MSG = f"Dubo | Examples: {DOCS_URL} | Discord: {FEEDBACK_URL} | Privacy policy: https://mercator.tech/privacy"

print(MSG)
