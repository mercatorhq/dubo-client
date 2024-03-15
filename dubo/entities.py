from dataclasses import dataclass
from typing import List

from dubo.api_client.models import QueryStatus


@dataclass
class DataResult:
    id: str
    query_text: str
    status: QueryStatus
    results_set: List[dict]
    row_count: int

    def validate(self) -> bool:
        if self.status not in [
            "running",
            "completed",
            "failed",
        ]:
            return False
        return True


@dataclass
class AutocompleteSqlResult:
    sql_query_full: str
    sql_query_suggested: str
