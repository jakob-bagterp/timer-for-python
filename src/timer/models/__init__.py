__all__ = ["Thread"]

from dataclasses import dataclass

@dataclass(frozen = True)
class Thread:
    """Class to define a thread's name, start time, and decimals"""

    name: str
    start_time: str
    decimals: int
