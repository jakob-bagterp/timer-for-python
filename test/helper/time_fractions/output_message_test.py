from timer.constants import none_value
from timer.helper.output import message
from timer.helper.time_fractions import TimeFractions
from timer.model.elapsed_time_fractions import ElapsedTimeFractions
from mock_data_time_fractions import random_days_as_ns, random_hours_as_ns, random_minutes_as_ns, random_seconds_as_ns, random_milliseconds_as_ns, random_microseconds_as_ns, random_nanoseconds_as_ns
from mock_data_output_message import random_decimals

def process_output_message(elapsed_time_ns: int, capfd: object, max_decimals: int = None) -> tuple[str, TimeFractions, ElapsedTimeFractions, int]:
    fractions = TimeFractions(elapsed_time_ns)
    time = fractions.time
    decimals = random_decimals() if max_decimals is None else random_decimals(max_decimals)
    message(none_value(), fractions, decimals)
    terminal_output, _ = capfd.readouterr()
    return terminal_output, fractions, time, decimals

class TestOutputMessage():
    def test_output_message_days(self, capfd):
        for _ in range(100):
            mock_elapsed_time_ns = random_days_as_ns(allow_zero = False)
            terminal_output, fractions, time, _ = process_output_message(mock_elapsed_time_ns, capfd)
            assert terminal_output == f"Elapsed time: {time.days}d {time.hours}h {time.minutes}m {fractions.seconds_rounded()}s\n"

    def test_output_message_hours(self, capfd):
        for _ in range(100):
            mock_elapsed_time_ns = random_hours_as_ns(allow_zero = False)
            terminal_output, fractions, time, _ = process_output_message(mock_elapsed_time_ns, capfd)
            assert terminal_output == f"Elapsed time: {time.hours}h {time.minutes}m {fractions.seconds_rounded()}s\n"

    def test_output_message_minutes(self, capfd):
        for _ in range(100):
            mock_elapsed_time_ns = random_minutes_as_ns(allow_zero = False)
            terminal_output, fractions, time, decimals = process_output_message(mock_elapsed_time_ns, capfd)
            assert terminal_output == f"Elapsed time: {fractions.count_minutes_to_seconds():.{decimals}f} seconds ({time.minutes}m {fractions.seconds_rounded()}s)\n"

    def test_output_message_seconds(self, capfd):
        for _ in range(100):
            mock_elapsed_time_ns = random_seconds_as_ns(allow_zero = False)
            terminal_output, fractions, _, decimals = process_output_message(mock_elapsed_time_ns, capfd)
            assert terminal_output == f"Elapsed time: {fractions.count_seconds_to_float():.{decimals}f} seconds\n"

    def test_output_message_milliseconds(self, capfd):
        for _ in range(100):
            mock_elapsed_time_ns = random_milliseconds_as_ns(allow_zero = False)
            terminal_output, fractions, _, decimals = process_output_message(mock_elapsed_time_ns, capfd)
            assert terminal_output == f"Elapsed time: {fractions.count_milliseconds_to_float():.{decimals}f} milliseconds\n"

    def test_output_message_microseconds(self, capfd):
        for _ in range(100):
            mock_elapsed_time_ns = random_microseconds_as_ns(allow_zero = False)
            terminal_output, fractions, _, decimals = process_output_message(mock_elapsed_time_ns, capfd)
            assert terminal_output == f"Elapsed time: {fractions.count_microseconds_to_float():.{decimals}f} microseconds\n"

    def test_output_message_nanoseconds(self, capfd):
        for _ in range(100):
            mock_elapsed_time_ns = random_nanoseconds_as_ns(allow_zero = False)
            terminal_output, _, time, _ = process_output_message(mock_elapsed_time_ns, capfd)
            assert terminal_output == f"Elapsed time: {time.nanoseconds} nanoseconds\n"
