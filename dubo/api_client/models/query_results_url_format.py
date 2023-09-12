from enum import Enum


class QueryResultsURLFormat(str, Enum):
    CSV = "csv"
    JSON = "json"
    PARQUET = "parquet"

    def __str__(self) -> str:
        return str(self.value)
