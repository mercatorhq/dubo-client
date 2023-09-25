from enum import Enum


class QueryStatus(str, Enum):
    FAILED = "failed"
    RUNNING = "running"
    SUCCESS = "success"

    def __str__(self) -> str:
        return str(self.value)
