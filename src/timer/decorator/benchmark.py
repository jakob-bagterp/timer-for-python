import functools
from collections.abc import Callable
from typing import Any

from ..model.timer import Timer


def benchmark_timer(thread: str | None = None, decimals: int = 2) -> Callable[..., Any]:
    def decorator(function: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(function)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            thread_name = thread if thread else function.__name__
            with Timer(thread=thread_name, decimals=decimals):
                return function(*args, **kwargs)
        return wrapper
    return decorator
