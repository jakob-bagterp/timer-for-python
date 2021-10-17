__all__ = ["ThreadItem"]

from dataclasses import dataclass

@dataclass(frozen = True)
class ThreadItem:
    """Class to define a thread's name, start time, and decimals"""

    name: str
    start_time: str
    decimals: int

@dataclass(frozen = True)
class ElapsedTimeFractions:
    """Class to define fractions of elapsed time"""

    nanoseconds: int
    microseconds: int
    microseconds: int
    seconds: int
    minutes: int
    hours: int
    days: int
