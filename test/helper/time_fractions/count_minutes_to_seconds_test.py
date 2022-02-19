from timer.helper.time_fractions import TimeFractions
from mock_data.time_fractions import random_minutes_as_ns

def test_count_minutes_to_seconds() -> None:
    float_precision = 6
    for _ in range(100):
        mock_elapsed_time_ns = random_minutes_as_ns()
        rounded_seconds = round(TimeFractions(mock_elapsed_time_ns).count_minutes_to_seconds(), float_precision)
        rounded_mock_seconds = round(mock_elapsed_time_ns / 1000 / 1000 / 1000, float_precision)
        assert rounded_seconds == rounded_mock_seconds
