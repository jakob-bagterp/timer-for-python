import functools
from collections.abc import Callable
from typing import Any

from ..model.abc.mkdocstrings import MkDocstringsWrapper_ABC
from ..model.timer import Timer


def function_timer(thread: str | None = None, decimals: int = 2) -> Callable[..., Any]:
    """Function decorator to measure the performance of a function."""

    def decorator(function: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(function)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            thread_name = thread if thread else function.__name__
            with Timer(thread=thread_name, decimals=decimals):
                return function(*args, **kwargs)
        return wrapper
    return decorator


class MkDocstringsWrapper(MkDocstringsWrapper_ABC):
    def function_timer(self, thread: str | None = None, decimals: int = 2) -> Callable[..., Any]:
        """Function decorator to measure the performance of a function.

        Args:
            thread (str | None, optional): Option to start new thread. By default, the thread name is the function name.
            decimals (int | None, optional): Option to define decimals for output. Minimum `0` (for no decimals) and maximum `9`. If `None`, default is `2` decimals. May be overruled in certain cases due to [humanised output](../user-guide/humanised-output.md).

        Example:
            Basic usage:

            ```python linenums="1" hl_lines="3"
            from timer import function_timer

            @function_timer()
            def test_function():
                # Insert your code here

            test_function()
            ```

            How it appears in the terminal:

            <pre><code>% Elapsed time: 12.34 seconds for thread <span class="fg-green">TEST_FUNCTION</span></code></pre>

            With custom thread name and decimals:

            ```python linenums="1" hl_lines="3"
            from timer import function_timer

            @function_timer(thread="custom", decimals=5)
            def test_function():
                # Insert your code here

            test_function()
            ```

            How it appears in the terminal:

            <pre><code>% Elapsed time: 0.12345 seconds for thread <span class="fg-green">CUSTOM</span></code></pre>
        """

        return function_timer(thread=thread, decimals=decimals)
