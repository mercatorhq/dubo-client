import time
from IPython.display import clear_output, display


class DuboException(Exception):
    def __init__(self, msg: str, *args: object) -> None:
        super().__init__(*args)

        self.msg = msg

    def __str__(self) -> str:
        return self.msg


def in_jupyter():
    try:
        from IPython.display import clear_output  # noqa

        return True
    except ImportError:
        return False


def loading_icon(duration=5):
    if not in_jupyter():
        return
    symbols = ["*---", "-*--", "--*-", "---*", "--*-", "-*--"]
    end_time = time.time() + duration

    while time.time() < end_time:
        for symbol in symbols:
            clear_output(wait=True)  # noqa
            display(symbol)
            time.sleep(0.2)
