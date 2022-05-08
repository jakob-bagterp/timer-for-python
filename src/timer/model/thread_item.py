from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ThreadItem:
    """Class to define a thread's name, start time, and decimals."""

    name: str
    start_time: int
    decimals: int
