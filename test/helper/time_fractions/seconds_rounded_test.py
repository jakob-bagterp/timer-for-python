import math

from _helper.time_fractions import random_seconds_as_ns

from timer.model.time_fractions import TimeFractions


def test_seconds_rounded() -> None:
    for _ in range(100):
        mock_elapsed_time_ns = random_seconds_as_ns()
        round_seconds = TimeFractions(mock_elapsed_time_ns).seconds_rounded()
        rounded_mock_seconds = round(mock_elapsed_time_ns / 1000 / 1000 / 1000, 0)
        assert math.isclose(round_seconds, rounded_mock_seconds, rel_tol=1e-9)
