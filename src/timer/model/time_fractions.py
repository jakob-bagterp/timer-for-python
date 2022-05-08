from .. import helper
from .elapsed_time_fractions import ElapsedTimeFractions


class TimeFractions:
    __slots__ = ["time"]

    def __init__(self, elapsed_time_ns: int) -> None:
        self.time: ElapsedTimeFractions = helper.time_fractions.calculate_time_fractions(elapsed_time_ns)

    def count_microseconds_to_float(self) -> float:
        return self.time.microseconds + self.time.nanoseconds / 1000

    def count_milliseconds_to_float(self) -> float:
        """This could potentially be faster by dividing self.microseconds by a 1000 directly, yet we don't want to lose precision in the decimals."""

        return self.time.milliseconds + self.count_microseconds_to_float() / 1000

    def count_seconds_to_float(self) -> float:
        """This could potentially be faster by dividing self.milliseconds by a 1000 directly, yet we don't want to lose precision in the decimals."""

        return self.time.seconds + self.count_milliseconds_to_float() / 1000

    def seconds_rounded(self) -> float:
        """For instance, if 2 seconds and 567 milliseconds, ensure it'll be rounded up to 3 seconds."""

        return int(round(self.count_seconds_to_float(), 0))

    def count_minutes_to_seconds(self) -> float:
        return self.time.minutes * 60 + self.count_seconds_to_float()
