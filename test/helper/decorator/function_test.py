import re
import time
from collections.abc import Callable

import pytest

from timer.decorator.function import function_timer

TEST_THREAD = "test"
TEST_DECIMALS = 5


def get_output_message_regex(thread: str, decimals: int = 2, time_unit: str = "milliseconds") -> str:
    """Generate regex pattern that matches, for example: `Elapsed time: 105.04 milliseconds for thread FUNCTION_TO_BE_TIMED`"""

    decimals_pattern = r"\d+\." + r"\d" * decimals if decimals > 0 else r"\d+"
    return rf"Elapsed time: {decimals_pattern} {time_unit} for thread \x1b\[32m{thread.upper()}\x1b\[0m\n"


@function_timer()
def function_to_be_timed(seconds: float) -> None:
    time.sleep(seconds)


@function_timer(thread=TEST_THREAD)
def function_to_be_timed_with_custom_thread(seconds: float) -> None:
    time.sleep(seconds)


@function_timer(decimals=TEST_DECIMALS)
def function_to_be_timed_with_custom_decimals(seconds: float) -> None:
    time.sleep(seconds)


@function_timer(thread=TEST_THREAD, decimals=TEST_DECIMALS)
def function_to_be_timed_with_custom_thread_and_decimals(seconds: float) -> None:
    time.sleep(seconds)


@pytest.mark.parametrize("function, thread, decimals", [
    (function_to_be_timed, None, None),
    (function_to_be_timed_with_custom_thread, TEST_THREAD, None),
    (function_to_be_timed_with_custom_decimals, None, TEST_DECIMALS),
    (function_to_be_timed_with_custom_thread_and_decimals, TEST_THREAD, TEST_DECIMALS),
])
def test_function_timer_decorator(function: Callable[[float], None], thread: str | None, decimals: int | None, capfd: object) -> None:
    _ = function(seconds=0.1)
    terminal_output, _ = capfd.readouterr()
    thread_name = thread if thread is not None else function.__name__
    output_message_regex = get_output_message_regex(thread_name, decimals) if decimals is not None else get_output_message_regex(thread_name)
    assert bool(re.fullmatch(output_message_regex, terminal_output)) is True
