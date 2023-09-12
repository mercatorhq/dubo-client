from enum import Enum


class ChatMessageTypes(str, Enum):
    CHAT = "chat"
    DECK_GL = "deck_gl"
    SQL = "sql"
    VEGA_LITE = "vega_lite"

    def __str__(self) -> str:
        return str(self.value)
