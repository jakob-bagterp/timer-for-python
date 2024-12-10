import re
import time
from collections.abc import Callable

import pytest
from _constant.interval import ULTRA_SHORT_INTERVAL
from _helper.terminal_output import successful_output_regex
from _helper.timer import ensure_all_timer_threads_are_stopped

from timer.decorator.function import function_timer

TEST_THREAD = "test"
TEST_DECIMALS = 5


@function_timer()
def function_to_be_timed() -> None:
    time.sleep(ULTRA_SHORT_INTERVAL)


@function_timer(thread=TEST_THREAD)
def function_to_be_timed_with_custom_thread() -> None:
    time.sleep(ULTRA_SHORT_INTERVAL)


@function_timer(decimals=TEST_DECIMALS)
def function_to_be_timed_with_custom_decimals() -> None:
    time.sleep(ULTRA_SHORT_INTERVAL)


@function_timer(thread=TEST_THREAD, decimals=TEST_DECIMALS)
def function_to_be_timed_with_custom_thread_and_decimals() -> None:
    time.sleep(ULTRA_SHORT_INTERVAL)


@pytest.mark.parametrize("function, thread, decimals", [
    (function_to_be_timed, None, None),
    (function_to_be_timed_with_custom_thread, TEST_THREAD, None),
    (function_to_be_timed_with_custom_decimals, None, TEST_DECIMALS),
    (function_to_be_timed_with_custom_thread_and_decimals, TEST_THREAD, TEST_DECIMALS),
])
def test_function_timer_decorator_for_function_without_arguments(function: Callable[..., None], thread: str | None, decimals: int | None, capfd: object) -> None:
    ensure_all_timer_threads_are_stopped()
    function()
    terminal_output, _ = capfd.readouterr()
    thread_name = thread if thread is not None else function.__name__
    expected_output_regex = successful_output_regex(thread_name, decimals) if decimals is not None else successful_output_regex(thread_name)
    assert re.fullmatch(expected_output_regex, terminal_output)
