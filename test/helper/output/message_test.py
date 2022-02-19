from colorist import Color
from timer.constant.various import NONE_VALUE
from timer.helper.output import message
from timer.helper.time_fractions import TimeFractions
from timer.model.elapsed_time_fractions import ElapsedTimeFractions
from helper.time_fractions.mock_data.time_fractions import random_days_as_ns, random_hours_as_ns, random_minutes_as_ns, random_seconds_as_ns, random_milliseconds_as_ns, random_microseconds_as_ns, random_nanoseconds_as_ns
from mock_data.output_message import random_decimals, random_thread_name

def process_terminal_message(elapsed_time_ns: int, capfd: object, max_decimals: int | None = None, has_thread: bool = False) -> tuple[str, TimeFractions, ElapsedTimeFractions, int, str]:
    fractions = TimeFractions(elapsed_time_ns)
    time = fractions.time
    decimals = random_decimals() if max_decimals is None else random_decimals(max_decimals)
    thread = NONE_VALUE if not has_thread else random_thread_name()
    message(thread, fractions, decimals)
    terminal_output, _ = capfd.readouterr()
    return terminal_output, fractions, time, decimals, thread

def test_output_message_days(capfd: object) -> None:
    for _ in range(100):
        mock_elapsed_time_ns = random_days_as_ns(allow_zero = False)
        terminal_output, fractions, time, _, _ = process_terminal_message(mock_elapsed_time_ns, capfd)
        assert terminal_output == f"Elapsed time: {time.days}d {time.hours}h {time.minutes}m {fractions.seconds_rounded()}s\n"

def test_output_message_hours(capfd: object) -> None:
    for _ in range(100):
        mock_elapsed_time_ns = random_hours_as_ns(allow_zero = False)
        terminal_output, fractions, time, _, _ = process_terminal_message(mock_elapsed_time_ns, capfd)
        assert terminal_output == f"Elapsed time: {time.hours}h {time.minutes}m {fractions.seconds_rounded()}s\n"

def test_output_message_minutes(capfd: object) -> None:
    for _ in range(100):
        mock_elapsed_time_ns = random_minutes_as_ns(allow_zero = False)
        terminal_output, fractions, time, decimals, _ = process_terminal_message(mock_elapsed_time_ns, capfd)
        assert terminal_output == f"Elapsed time: {fractions.count_minutes_to_seconds():.{decimals}f} seconds ({time.minutes}m {fractions.seconds_rounded()}s)\n"

def test_output_message_seconds(capfd: object) -> None:
    for _ in range(100):
        mock_elapsed_time_ns = random_seconds_as_ns(allow_zero = False)
        terminal_output, fractions, _, decimals, _ = process_terminal_message(mock_elapsed_time_ns, capfd)
        assert terminal_output == f"Elapsed time: {fractions.count_seconds_to_float():.{decimals}f} seconds\n"

def test_output_message_milliseconds(capfd: object) -> None:
    for _ in range(100):
        mock_elapsed_time_ns = random_milliseconds_as_ns(allow_zero = False)
        terminal_output, fractions, _, decimals, _ = process_terminal_message(mock_elapsed_time_ns, capfd)
        assert terminal_output == f"Elapsed time: {fractions.count_milliseconds_to_float():.{decimals}f} milliseconds\n"

def test_output_message_microseconds(capfd: object) -> None:
    for _ in range(100):
        mock_elapsed_time_ns = random_microseconds_as_ns(allow_zero = False)
        terminal_output, fractions, _, decimals, _ = process_terminal_message(mock_elapsed_time_ns, capfd)
        assert terminal_output == f"Elapsed time: {fractions.count_microseconds_to_float():.{decimals}f} microseconds\n"

def test_output_message_nanoseconds(capfd: object) -> None:
    for _ in range(100):
        mock_elapsed_time_ns = random_nanoseconds_as_ns(allow_zero = False)
        terminal_output, _, time, _, _ = process_terminal_message(mock_elapsed_time_ns, capfd)
        assert terminal_output == f"Elapsed time: {time.nanoseconds} nanoseconds\n"

def test_output_message_hours_with_custom_thread(capfd: object) -> None:
    for _ in range(100):
        mock_elapsed_time_ns = random_hours_as_ns(allow_zero = False)
        terminal_output, fractions, time, _, thread = process_terminal_message(mock_elapsed_time_ns, capfd, has_thread = True)
        assert terminal_output == f"Elapsed time (thread {Color.GREEN}{thread}{Color.OFF}): {time.hours}h {time.minutes}m {fractions.seconds_rounded()}s\n"
