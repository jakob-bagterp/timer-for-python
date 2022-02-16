from enum import Enum

class Colour(Enum):
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    RESET = "\033[0m"

    def __str__(self) -> str:
        return str(self.value)
