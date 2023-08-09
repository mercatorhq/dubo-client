from dataclasses import dataclass
from typing import List


@dataclass
class DataResult:
    id: str
    query_text: str
    status: str
    results_set: List[dict]
    row_count: int

    def validate(self) -> bool:
        if self.status not in [
            "running",
            "completed",
            "failed",
        ]:
            return False
        return True
