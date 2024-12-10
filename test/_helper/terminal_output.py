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
    """Now that we don't know the time, we can't predict the output. We can only check that the pattern of the output is correct, especially the dynamic part of measured time.

    This method generates a regex pattern for the expected output that matches, for example, `Elapsed time: 123.45 milliseconds for thread CUSTOM` or `Elapsed time: 123.45 milliseconds`"""

    decimals_pattern = r"\d+\." + r"\d" * decimals if decimals > 0 else r"\d+"
    thread_info = rf" for thread \x1b\[32m{thread.upper()}\x1b\[0m" if thread is not None else ""
    return rf"Elapsed time: {decimals_pattern} {time_unit}{thread_info}\n"
