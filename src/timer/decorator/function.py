import functools
from collections.abc import Callable
from typing import Any

from ..model.abc.mkdocstrings import MkDocstringsWrapper_ABC
from ..model.timer import Timer


def function_timer(thread: str | None = None, decimals: int = 2) -> Callable[..., Any]:
    """Function decorator to measure the performance of a function."""

    def get_function_with_arguments_as_thread_name(function: Callable[..., Any], args: tuple[Any, ...], kwargs: dict[str, Any]) -> str:
        thread_name = function.__name__
        if args or kwargs:
            arg_names = function.__code__.co_varnames[:function.__code__.co_argcount]
            mapped_args = [f"{name}={value!r}" for name, value in zip(arg_names, args)]
            mapped_kwargs = [f"{key}={value!r}" for key, value in kwargs.items()]
            all_mapped_args = ", ".join(mapped_args + mapped_kwargs)
            thread_name += f"({all_mapped_args})"
        return thread_name

    def decorator(function: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(function)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            thread_name = thread if thread else get_function_with_arguments_as_thread_name(function, args, kwargs)
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

            The `@function_timer` automatically names the function and its arguments as thread name. For example:

            ```python linenums="1" hl_lines="3-4"
            from timer import function_timer

            @function_timer()
            def sum_numbers(a, b):
                return a + b

            sum_numbers(1, 2)
            ```

            How it appears in the terminal:

            <pre><code>% Elapsed time: 0.12 seconds for thread <span class="fg-green">SUM_NUMBERS(A=1, B=2)</span></code></pre>
        """

        return function_timer(thread=thread, decimals=decimals)  # pragma: no cover
