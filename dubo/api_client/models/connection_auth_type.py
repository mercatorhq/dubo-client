from enum import Enum


class ConnectionAuthType(str, Enum):
    CERTIFICATE = "certificate"
    PASSWORD = "password"

    def __str__(self) -> str:
        return str(self.value)
