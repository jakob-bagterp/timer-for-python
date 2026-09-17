from .. import helper
from ..constant.various import SECONDS_PER_MINUTE
from .elapsed_time_fractions import ElapsedTimeFractions


class TimeFractions:
    __slots__ = ["time"]

    def __init__(self, elapsed_time_ns: int) -> None:
        self.time: ElapsedTimeFractions = helper.time_fractions.calculate_time_fractions(elapsed_time_ns)

    def total_microseconds(self) -> float:
        return self.time.microseconds + self.time.nanoseconds / 1_000

    def total_milliseconds(self) -> float:
        """This could potentially be faster by dividing self.microseconds by a 1,000 directly, yet we don't want to lose precision in the decimals."""

        return self.time.milliseconds + self.total_microseconds() / 1_000

    def total_seconds(self) -> float:
        """This could potentially be faster by dividing self.milliseconds by a 1,000 directly, yet we don't want to lose precision in the decimals."""

        return self.time.seconds + self.total_milliseconds() / 1_000

    def seconds_rounded(self) -> float:
        """For instance, if 2 seconds and 567 milliseconds, ensure it'll be rounded up to 3 seconds."""

        return int(round(self.total_seconds(), 0))

    def total_minutes_as_seconds(self) -> float:
        return self.time.minutes * SECONDS_PER_MINUTE + self.total_seconds()
