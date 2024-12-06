import functools
from collections.abc import Callable
from typing import Any

from ..model.timer import Timer


def function_timer(thread: str | None = None, decimals: int = 2) -> Callable[..., Any]:
    """Function decorator to measure the performance of a function.

    Args:
        thread (str | None, optional): Option to start new thread.
        decimals (int | None, optional): Option to define decimals for output. Minimum `0` (for no decimals) and maximum `9`. If `None`, default is `2` decimals. May be overruled in certain cases due to [humanised output](../user-guide/humanised-output.md).

    Example:
        Basic usage:

        ```python linenums="1" hl_lines="3"
        from timer import function_timer

        @function_timer
        def test_function():
            # Insert your code here

        test_function()
        ```

        Terminal output example:

        ```text title=""
        Elapsed time: 12.34 seconds for thread TEST_FUNCTION
        ```

        With custom thread name and decimals:

        ```python linenums="1" hl_lines="3"
        from timer import function_timer

        @function_timer(thread="A", decimals=5)
        def test_function():
            # Insert your code here

        test_function()
        ```

        Terminal output example:

        ```text title=""
        Elapsed time: 0.12345 seconds for thread A
        ```
    """

    def decorator(function: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(function)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            thread_name = thread if thread else function.__name__
            with Timer(thread=thread_name, decimals=decimals):
                return function(*args, **kwargs)
        return wrapper
    return decorator
