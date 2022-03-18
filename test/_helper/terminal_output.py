import re

DECIMALS_PATTERN = re.compile(r"(?<=\.)\d*")


def verify_decimals_in_terminal_output(decimals: int, terminal_output: str) -> bool:
    decimals_output = DECIMALS_PATTERN.search(terminal_output)
    if decimals == 0:
        return decimals_output is None
    else:
        return decimals == len(decimals_output.group(0))
