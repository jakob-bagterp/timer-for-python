from enum import Enum, unique


@unique
class TimeUnit(Enum):
    """Time unit options for the Timer."""

    NANOSECONDS = "nanoseconds"
    MICROSECONDS = "microseconds"
    MILLISECONDS = "milliseconds"
    SECONDS = "seconds"
    MINUTES = "minutes"
    HOURS = "hours"
    DAYS = "days"

    def __str__(self) -> str:
        return str(self.value)
