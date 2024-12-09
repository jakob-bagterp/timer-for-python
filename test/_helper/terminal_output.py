import re

DECIMALS_PATTERN = re.compile(r"(?<=\.)\d*")  # Captures "456789" from "Elapsed time: 123.456789 milliseconds".


def verify_decimals_in_terminal_output(decimals: int, terminal_output: str) -> bool:
    decimals_output = DECIMALS_PATTERN.search(terminal_output)
    if decimals == 0:
        return decimals_output is None
    else:
        return decimals == len(decimals_output.group(0))


PREFIX_PATTERN = re.compile(r"^Elapsed time")


def verify_prefix_in_terminal_output(terminal_output: str) -> bool:
    return bool(PREFIX_PATTERN.match(terminal_output))


def successful_output_regex(thread: str | None = None, decimals: int = 2, time_unit: str = "milliseconds") -> str:
    """Generate regex pattern for the expected output that matches, for example, `Elapsed time: 105.04 milliseconds for thread FUNCTION_TO_BE_TIMED` or `Elapsed time: 105.04 milliseconds`"""

    decimals_pattern = r"\d+\." + r"\d" * decimals if decimals > 0 else r"\d+"
    thread_info = rf" for thread \x1b\[32m{thread.upper()}\x1b\[0m" if thread is not None else ""
    return rf"Elapsed time: {decimals_pattern} {time_unit}{thread_info}\n"
