from enum import Enum


class ChartType(str, Enum):
    DECK_GL = "deck_gl"
    VEGA_LITE = "vega_lite"

    def __str__(self) -> str:
        return str(self.value)
