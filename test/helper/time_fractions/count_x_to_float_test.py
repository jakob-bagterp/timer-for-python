import math

from _helper.time_fractions import random_microseconds_as_ns, random_milliseconds_as_ns, random_seconds_as_ns

from timer.model.time_fractions import TimeFractions


def test_count_microseconds_to_float() -> None:
    float_precision = 6
    for _ in range(1000):
        mock_elapsed_time_ns = random_microseconds_as_ns()
        rounded_microseconds_to_float = round(TimeFractions(
            mock_elapsed_time_ns).count_microseconds_to_float(), float_precision)
        rounded_mock_microseconds_to_float = round(mock_elapsed_time_ns / 1000, float_precision)
        assert math.isclose(rounded_microseconds_to_float, rounded_mock_microseconds_to_float, rel_tol=1e-6)


def test_count_milliseconds_to_float() -> None:
    float_precision = 9
    for _ in range(1000):
        mock_elapsed_time_ns = random_milliseconds_as_ns()
        rounded_milliseconds_to_float = round(TimeFractions(
            mock_elapsed_time_ns).count_milliseconds_to_float(), float_precision)
        rounded_mock_milliseconds_to_float = round(mock_elapsed_time_ns / 1000 / 1000, float_precision)
        assert math.isclose(rounded_milliseconds_to_float, rounded_mock_milliseconds_to_float, rel_tol=1e-9)


def test_count_seconds_to_float() -> None:
    float_precision = 12
    for _ in range(1000):
        mock_elapsed_time_ns = random_seconds_as_ns()
        rounded_seconds_to_float = round(TimeFractions(mock_elapsed_time_ns).count_seconds_to_float(), float_precision)
        rounded_mock_seconds_to_float = round(mock_elapsed_time_ns / 1000 / 1000 / 1000, float_precision)
        assert math.isclose(rounded_seconds_to_float, rounded_mock_seconds_to_float, rel_tol=1e-12)
