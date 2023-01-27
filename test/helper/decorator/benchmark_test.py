import re
import time

from timer.decorator.benchmark import benchmark_timer

# Mathes pattern: "Elapsed time (thread \x1b[32mFUNCTION_TO_BE_BENCHMARKED\x1b[0m): 105.04 milliseconds\n"
OUTPUT_MESSAGE_REGEX = r"Elapsed time \(thread [\Wx1b]\[32mFUNCTION_TO_BE_BENCHMARKED[\Wx1b]\[0m\): \d+\.\d\d milliseconds[\Wn]"


@benchmark_timer
def function_to_be_benchmarked(seconds: float) -> None:
    time.sleep(seconds)


def test_benchmark_timer_decorator(capfd: object) -> None:
    _ = function_to_be_benchmarked(seconds=0.1)
    terminal_output, _ = capfd.readouterr()
    assert bool(re.fullmatch(OUTPUT_MESSAGE_REGEX, terminal_output)) is True
