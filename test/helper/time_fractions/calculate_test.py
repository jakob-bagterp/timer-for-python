from _helper.time_fractions import random_elapsed_time_ns_and_fractions

from timer.helper.time_fractions import calculate_time_fractions


def test_calculate_time_fractions() -> None:
    for _ in range(100000):
        mock_elapsed_time_ns, mock_elapsed_time_fractions = random_elapsed_time_ns_and_fractions()
        assert calculate_time_fractions(mock_elapsed_time_ns) == mock_elapsed_time_fractions
