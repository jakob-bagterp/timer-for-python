from timer.helper.time_fractions import calculate_time_fractions
from mock_data_time_fractions import random_elapsed_time_ns_and_fractions

class TestCalculateTimeFractions():
    def test_calculate_time_fractions(self) -> None:
        for _ in range(100000):
            mock_elapsed_time_ns, mock_elapsed_time_fractions = random_elapsed_time_ns_and_fractions()
            assert calculate_time_fractions(mock_elapsed_time_ns) == mock_elapsed_time_fractions
