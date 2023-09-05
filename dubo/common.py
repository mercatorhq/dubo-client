class DuboException(Exception):
    def __init__(self, msg: str, *args: object) -> None:
        super().__init__(*args)

        self.msg = msg

    def __str__(self) -> str:
        return self.msg
