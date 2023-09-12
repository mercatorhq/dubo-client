from enum import Enum


class UserRole(str, Enum):
    ADMIN = "admin"
    AUTHOR = "author"
    READER = "reader"

    def __str__(self) -> str:
        return str(self.value)
