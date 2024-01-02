from enum import Enum


class CreateApiQueryMode(str, Enum):
    FULL_EXECUTION = "full_execution"
    IMMEDIATE_EXECUTION = "immediate_execution"
    JUST_SQL_TEXT = "just_sql_text"
    JUST_TABLES = "just_tables"

    def __str__(self) -> str:
        return str(self.value)
