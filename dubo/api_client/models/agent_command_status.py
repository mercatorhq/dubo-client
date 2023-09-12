from enum import Enum


class AgentCommandStatus(str, Enum):
    COMPLETED = "completed"
    ERROR = "error"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
