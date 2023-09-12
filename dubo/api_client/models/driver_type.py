from enum import Enum


class DriverType(str, Enum):
    BIGQUERY = "bigquery"
    POSTGRESQL = "postgresql"
    SNOWFLAKE = "snowflake"

    def __str__(self) -> str:
        return str(self.value)
