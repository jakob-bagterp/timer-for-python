import re

from _constant.time_unit import TimeUnit

elapsed_time_pattern = re.compile(r"(?<=\.)\d*")  # Captures "456789" from "Elapsed time: 123.456789 milliseconds".


def verify_decimals_in_terminal_output(decimals: int, terminal_output: str) -> bool:
    decimals_output = elapsed_time_pattern.search(terminal_output)
    if decimals == 0:
        return decimals_output is None
    else:
        return decimals == len(decimals_output.group(0))


PREFIX_PATTERN = re.compile(r"^Elapsed time")


def verify_prefix_in_terminal_output(terminal_output: str) -> bool:
    return bool(PREFIX_PATTERN.match(terminal_output))


def successful_output_regex(thread: str | None = None, decimals: int = 2, time_unit: TimeUnit = TimeUnit.MILLISECONDS) -> str:
    """Now that we don't know the elapsed time, we can't predict the output. We can only check that the pattern of the output is correct, especially the dynamic part of elapsed time.

    This method generates a regex pattern for the expected output that matches, for example, `Elapsed time: 123.45 milliseconds` or with a custom thread `Elapsed time: 123.45 milliseconds for thread CUSTOM`"""

    decimals_pattern = rf"\.\d{{{decimals}}}" if decimals > 0 else ""
    microseconds_to_seconds_elapsed_time_pattern = rf"\d+{decimals_pattern} {time_unit}"
    match time_unit:
        case TimeUnit.NANOSECONDS:
            elapsed_time_pattern = r"\d+ nanoseconds"
        case TimeUnit.SECONDS:
            elapsed_time_pattern = rf"{microseconds_to_seconds_elapsed_time_pattern}( \(\d+m \d+s\))?"
        case TimeUnit.MINUTES:
            elapsed_time_pattern = rf"\d+{decimals_pattern} {TimeUnit.SECONDS} \(\d+m \d+s\)"
        case TimeUnit.HOURS:
            elapsed_time_pattern = r"\d+h \d+m \d+s"
        case TimeUnit.DAYS:
            elapsed_time_pattern = r"\d+d \d+h \d+m \d+s"
        case _:
            elapsed_time_pattern = microseconds_to_seconds_elapsed_time_pattern
    thread_info = rf" for thread \x1b\[32m{thread.upper()}\x1b\[0m" if thread is not None else ""
    return rf"Elapsed time: {elapsed_time_pattern}{thread_info}\n"
