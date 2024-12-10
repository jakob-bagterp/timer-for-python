import re
import time
from collections.abc import Callable
from typing import Any

import pytest
from _helper.terminal_output import successful_output_regex
from _helper.timer import ensure_all_timer_threads_are_stopped

from timer.decorator.function import function_timer

TEST_THREAD = "test"
TEST_DECIMALS = 5
ULTRA_SHORT_DELAY = 0.001


@function_timer()
def function_with_args(a: int, b: int) -> None:
    time.sleep(ULTRA_SHORT_DELAY)


@function_timer()
def function_with_kwargs(x: int = 1, y: int = 2) -> None:
    time.sleep(ULTRA_SHORT_DELAY)


@function_timer()
def function_with_args_and_kwargs(a: int, b: int, x: int = 3, y: int = 4) -> None:
    time.sleep(ULTRA_SHORT_DELAY)


@pytest.mark.parametrize("function, args, kwargs, expected_thread_name", [
    (function_with_args, (1, 2), {}, "FUNCTION_WITH_ARGS(A=1, B=2)"),
    (function_with_kwargs, (), {"x": 3, "y": 4}, "FUNCTION_WITH_KWARGS(X=3, Y=4)"),
    (function_with_args_and_kwargs, (1, 2), {"x": 3, "y": 4}, "FUNCTION_WITH_ARGS_AND_KWARGS(A=1, B=2, X=3, Y=4)"),
])
def test_function_timer_decorator_for_function_with_arguments(function: Callable[..., None], args: tuple[Any, ...], kwargs: dict[str, Any], expected_thread_name: str, capfd: object) -> None:
    ensure_all_timer_threads_are_stopped()
    function(*args, **kwargs)
    terminal_output, _ = capfd.readouterr()
    expected_output_regex = successful_output_regex(thread=expected_thread_name)
    assert re.fullmatch(expected_output_regex, terminal_output)
