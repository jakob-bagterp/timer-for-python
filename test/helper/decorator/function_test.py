import re
import time

from timer.decorator.function import function_timer

# Mathes pattern: "Elapsed time (thread \x1b[32mFUNCTION_TO_BE_TIMED\x1b[0m): 105.04 milliseconds\n"
OUTPUT_MESSAGE_REGEX = r"Elapsed time \(thread [\Wx1b]\[32mFUNCTION_TO_BE_TIMED[\Wx1b]\[0m\): \d+\.\d\d milliseconds[\Wn]"


@function_timer
def function_to_be_timed(seconds: float) -> None:
    time.sleep(seconds)


def test_function_timer_decorator(capfd: object) -> None:
    _ = function_to_be_timed(seconds=0.1)
    terminal_output, _ = capfd.readouterr()
    assert bool(re.fullmatch(OUTPUT_MESSAGE_REGEX, terminal_output)) is True
