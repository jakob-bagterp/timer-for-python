import re
import time
from collections.abc import Callable

import pytest
from _constant.interval import ONE_MILLISECOND_AS_SECOND
from _helper.terminal_output import successful_output_regex
from _helper.timer import ensure_all_timer_threads_are_stopped

from timer.decorator.function import function_timer

CUSTOM_THREAD = "custom"
CUSTOM_DECIMALS = 5


@function_timer()
def function_to_be_timed() -> None:
    time.sleep(ONE_MILLISECOND_AS_SECOND)


@function_timer(thread=CUSTOM_THREAD)
def function_to_be_timed_with_custom_thread() -> None:
    time.sleep(ONE_MILLISECOND_AS_SECOND)


@function_timer(decimals=CUSTOM_DECIMALS)
def function_to_be_timed_with_custom_decimals() -> None:
    time.sleep(ONE_MILLISECOND_AS_SECOND)


@function_timer(thread=CUSTOM_THREAD, decimals=CUSTOM_DECIMALS)
def function_to_be_timed_with_custom_thread_and_decimals() -> None:
    time.sleep(ONE_MILLISECOND_AS_SECOND)


@pytest.mark.parametrize("function, thread, decimals", [
    (function_to_be_timed, None, None),
    (function_to_be_timed_with_custom_thread, CUSTOM_THREAD, None),
    (function_to_be_timed_with_custom_decimals, None, CUSTOM_DECIMALS),
    (function_to_be_timed_with_custom_thread_and_decimals, CUSTOM_THREAD, CUSTOM_DECIMALS),
])
def test_function_timer_decorator_for_function_without_arguments(function: Callable[..., None], thread: str | None, decimals: int | None, capfd: object) -> None:
    ensure_all_timer_threads_are_stopped()
    function()
    terminal_output, _ = capfd.readouterr()
    thread_name = thread if thread is not None else function.__name__
    expected_output_regex = successful_output_regex(thread_name, decimals) if decimals is not None else successful_output_regex(thread_name)
    assert re.fullmatch(expected_output_regex, terminal_output)
