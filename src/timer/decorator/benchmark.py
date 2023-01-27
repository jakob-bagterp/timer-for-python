import functools
from collections.abc import Callable
from typing import Any

from ..model.timer import Timer


def benchmark_timer(function: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(function)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        with Timer(thread=function.__name__):
            return function(*args, **kwargs)

    return wrapper
