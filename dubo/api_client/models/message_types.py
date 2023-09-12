from enum import Enum


class MessageTypes(str, Enum):
    CHART = "chart"
    CHAT = "chat"
    QUERY = "query"

    def __str__(self) -> str:
        return str(self.value)
