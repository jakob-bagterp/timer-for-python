from timer.constants import none_value
from timer.helper.output import message
from timer.helper.time_fractions import TimeFractions
from mock_data_time_fractions import random_days_as_ns, random_hours_as_ns, random_minutes_as_ns
from mock_data_output_message import random_decimals

class TestOutputMessage():
    def test_output_message_days(self, capfd):
        for _ in range(100):
            mock_elapsed_time_ns = random_days_as_ns(allow_zero = False)
            fractions = TimeFractions(mock_elapsed_time_ns)
            time = fractions.time
            decimals = random_decimals()
            message(none_value(), fractions, decimals)
            terminal_output, _ = capfd.readouterr()
            assert terminal_output == f"Elapsed time: {time.days}d {time.hours}h {time.minutes}m {fractions.seconds_rounded()}s\n"

    def test_output_message_hours(self, capfd):
        for _ in range(100):
            mock_elapsed_time_ns = random_hours_as_ns(allow_zero = False)
            fractions = TimeFractions(mock_elapsed_time_ns)
            time = fractions.time
            decimals = random_decimals()
            message(none_value(), fractions, decimals)
            terminal_output, _ = capfd.readouterr()
            assert terminal_output == f"Elapsed time: {time.hours}h {time.minutes}m {fractions.seconds_rounded()}s\n"

    def test_output_message_minutes(self, capfd):
        for _ in range(100):
            mock_elapsed_time_ns = random_minutes_as_ns(allow_zero = False)
            fractions = TimeFractions(mock_elapsed_time_ns)
            time = fractions.time
            decimals = random_decimals()
            message(none_value(), fractions, decimals)
            terminal_output, _ = capfd.readouterr()
            assert terminal_output == f"Elapsed time: {fractions.count_minutes_to_seconds():.{decimals}f} seconds ({time.minutes}m {fractions.seconds_rounded()}s)\n"
