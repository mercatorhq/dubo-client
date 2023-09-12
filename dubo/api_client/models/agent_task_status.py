from enum import Enum


class AgentTaskStatus(str, Enum):
    CANCELED = "canceled"
    COMPLETED = "completed"
    ERROR = "error"
    RUNNING = "running"
    STARTING = "starting"

    def __str__(self) -> str:
        return str(self.value)
