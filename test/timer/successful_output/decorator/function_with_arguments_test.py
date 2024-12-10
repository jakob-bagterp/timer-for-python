import re
import time
from collections.abc import Callable
from typing import Any

import pytest
from _constant.interval import ULTRA_SHORT_INTERVAL
from _helper.terminal_output import successful_output_regex
from _helper.timer import ensure_all_timer_threads_are_stopped

from timer.constant.decimals import DEFAULT as DEFAULT_DECIMALS
from timer.decorator.function import function_timer

CUSTOM_THREAD = "custom"
CUSTOM_DECIMALS = 5


@function_timer()
def function_with_args(a: int, b: int) -> None:
    time.sleep(ULTRA_SHORT_INTERVAL)


@function_timer()
def function_with_kwargs(x: int = 1, y: int = 2) -> None:
    time.sleep(ULTRA_SHORT_INTERVAL)


@function_timer()
def function_with_args_and_kwargs(a: int, b: int, x: int = 3, y: int = 4) -> None:
    time.sleep(ULTRA_SHORT_INTERVAL)


@function_timer()
def function_with_args_and_kwargs_number_and_strings(a: int, b: str, x: int = 3, y: str = "4") -> None:
    time.sleep(ULTRA_SHORT_INTERVAL)


@function_timer(thread=CUSTOM_THREAD)
def function_with_args_kwargs_and_custom_thread(a: int, b: int, x: int = 3, y: int = 4) -> None:
    time.sleep(ULTRA_SHORT_INTERVAL)


@function_timer(thread=CUSTOM_THREAD, decimals=CUSTOM_DECIMALS)
def function_with_args_kwargs_custom_thread_and_custom_decimals(a: int, b: int, x: int = 3, y: int = 4) -> None:
    time.sleep(ULTRA_SHORT_INTERVAL)


@pytest.mark.parametrize("function, args, kwargs, expected_thread_name, decimals", [
    (function_with_args, (1, 2), {}, "FUNCTION_WITH_ARGS(A=1, B=2)", DEFAULT_DECIMALS),
    (function_with_kwargs, (), {"x": 3, "y": 4}, "FUNCTION_WITH_KWARGS(X=3, Y=4)", DEFAULT_DECIMALS),
    (function_with_args_and_kwargs, (1, 2), {"x": 3, "y": 4}, "FUNCTION_WITH_ARGS_AND_KWARGS(A=1, B=2, X=3, Y=4)", DEFAULT_DECIMALS),
    (function_with_args_and_kwargs_number_and_strings, (1, "2"), {"x": 3, "y": "4"}, "FUNCTION_WITH_ARGS_AND_KWARGS_NUMBER_AND_STRINGS(A=1, B='2', X=3, Y='4')", DEFAULT_DECIMALS),
    (function_with_args_kwargs_and_custom_thread, (1, 2), {"x": 3, "y": 4}, CUSTOM_THREAD, DEFAULT_DECIMALS),
    (function_with_args_kwargs_custom_thread_and_custom_decimals, (1, 2), {"x": 3, "y": 4}, CUSTOM_THREAD, CUSTOM_DECIMALS),
])
def test_function_timer_decorator_for_function_with_arguments(function: Callable[..., None], args: tuple[Any, ...], kwargs: dict[str, Any], expected_thread_name: str, decimals: int, capfd: object) -> None:
    ensure_all_timer_threads_are_stopped()
    function(*args, **kwargs)
    terminal_output, _ = capfd.readouterr()
    expected_output_regex = successful_output_regex(thread=expected_thread_name, decimals=decimals)
    assert re.fullmatch(expected_output_regex, terminal_output)
