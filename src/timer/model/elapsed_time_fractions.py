from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ElapsedTimeFractions:
    """Class to define fractions of elapsed time."""

    nanoseconds: int
    microseconds: int
    milliseconds: int
    seconds: int
    minutes: int
    hours: int
    days: int
