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
