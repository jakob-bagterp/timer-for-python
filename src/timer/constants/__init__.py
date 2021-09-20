__all__ = ["Constants"]

class Decimals:
    def __init__(self) -> None:
        self.default = 2

class ListKey:
    def __init__(self) -> None:
        self.thread = "thread"
        self.start_time = "start_time"
        self.decimals = "decimals"

class Constants:
    def __init__(self) -> None:
        self.none_value = "NONE" # NB: Has to be string and upppercase.
        self.list_key = ListKey()
        self.decimals = Decimals()
