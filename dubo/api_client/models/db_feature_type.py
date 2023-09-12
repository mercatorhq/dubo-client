from enum import Enum


class DbFeatureType(str, Enum):
    CANCELLATIONS = "cancellations"

    def __str__(self) -> str:
        return str(self.value)
