from __future__ import annotations

import time
from types import TracebackType

from .. import constant, controller, error, helper
from .thread_item import ThreadItem
from .timer_base import TimerBase


class Timer(TimerBase):
    __slots__ = ["_threads", "_decimals",
                 "_context_manager_threads", "_context_manager_latest_thread", "_context_manager_latest_decimals",
                 "__dict__"]

    _instance = None
    _lock_init = False

    def __new__(cls, thread: str | None = None, decimals: int = constant.decimals.DEFAULT) -> TimerBase:  # type: ignore
        if not cls._instance:  # Singleton: Ensure there's only a single instance of Timer running.
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, thread: str | None = None, decimals: int = 2) -> None:
        """Main class to create a Timer instance. If not using the class with a `with` statement as [context manager](../user-guide/context-manager.md), remember that a `timer.start()` should always be followed by `timer.stop()` later in the code.

        Args:
            thread (str | None, optional): Option to start new thread.
            decimals (int | None, optional): Option to define decimals for output. Minimum `0` (for no decimals) and maximum `9`. If `None`, default is `2` decimals. May be overruled in certain cases due to [humanised output](../user-guide/humanised-output.md).

        Example:
            Basic usage:

            ```python linenums="1" hl_lines="3"
            from timer import Timer

            timer = Timer()
            timer.start()

            # Insert your code here

            timer.stop()
            ```

            Or with a `with` statement as [context manager](../user-guide/context-manager.md):

            ```python linenums="1" hl_lines="3"
            from timer import Timer

            with Timer():
                # Insert your code here
            ```

            In both cases, the terminal output example is the same:

            ```text title=""
            Elapsed time: 12.34 seconds
            ```

            With custom thread name and decimals:

            ```python linenums="1" hl_lines="3"
            from timer import Timer

            timer = Timer(thread="custom", decimals=5)
            timer.start()

            # Insert your code here

            timer.stop(thread="custom")
            ```

            Or with a `with` statement as [context manager](../user-guide/context-manager.md):

            ```python linenums="1" hl_lines="3"
            from timer import Timer

            with Timer(thread="custom", decimals=5):
                # Insert your code here
            ```

            As before, the terminal will output the same result in both cases:

            <pre><code>% Elapsed time: 0.12345 seconds for thread <span class="fg-green">CUSTOM</span></code></pre>
        """

        if not self._lock_init:  # Ensure that initialisation of the lists only runs the first time.
            self._threads: list[ThreadItem] = []
            self._context_manager_threads: list[str] = []
            self._lock_init = True
        self._decimals: int = decimals if decimals == constant.decimals.DEFAULT else helper.decimals.validate_and_normalise(
            decimals)
        self._context_manager_latest_thread: str = helper.thread.normalise_to_string_and_uppercase(thread)
        self._context_manager_latest_decimals: int = self._decimals

    def __enter__(self) -> Timer:
        self._context_manager_threads.append(self._context_manager_latest_thread)
        self.start(self._context_manager_latest_thread, self._context_manager_latest_decimals)
        return self

    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None) -> None:
        last_context_manager_thread = self._context_manager_threads.pop()
        self.stop(last_context_manager_thread)

    def start(self, thread: str | None = None, decimals: int | None = None) -> None:
        """Starts the Timer. Should always be followed by `timer.stop()` later in the code.

        Args:
            thread (str | None, optional): Option to start new thread.
            decimals (int | None, optional): Option to define decimals for output. Minimum `0` (for no decimals) and maximum `9`. If `None`, default is `2` decimals. May be overruled in certain cases due to [humanised output](../user-guide/humanised-output.md).

        Example:
            Basic usage:

            ```python linenums="1" hl_lines="4"
            from timer import Timer

            timer = Timer()
            timer.start()

            # Insert your code here

            timer.stop()
            ```

            How it appears in the terminal:

            ```text title=""
            Elapsed time: 12.34 seconds
            ```

            With custom thread name and decimals:

            ```python linenums="1" hl_lines="4"
            from timer import Timer

            timer = Timer()
            timer.start(thread="custom", decimals=5)

            # Insert your code here

            timer.stop(thread="custom")
            ```

            How it appears in the terminal:

            <pre><code>% Elapsed time: 0.12345 seconds for thread <span class="fg-green">CUSTOM</span></code></pre>
        """

        try:
            start_time = time.perf_counter_ns()  # For precision, this is the first operation of the function.
            controller.start(self, thread, start_time, decimals)
        except Exception:  # pragma: no cover
            error.message_for_action("when trying to start the Timer", thread)  # pragma: no cover

    def stop(self, thread: str | None = None) -> None:
        """Stops the Timer. Should always be called after `timer.start()`.

        Args:
            thread (str | None, optional): Option to stop specific thread.

        Example:
            Basic usage:

            ```python linenums="1" hl_lines="8"
            from timer import Timer

            timer = Timer()
            timer.start()

            # Insert your code here

            timer.stop()
            ```

            How it appears in the terminal:

            ```text title=""
            Elapsed time: 12.34 seconds
            ```

            With custom thread name and decimals:

            ```python linenums="1" hl_lines="8"
            from timer import Timer

            timer = Timer()
            timer.start(thread="custom", decimals=5)

            # Insert your code here

            timer.stop(thread="custom")
            ```

            How it appears in the terminal:

            <pre><code>% Elapsed time: 0.12345 seconds for thread <span class="fg-green">CUSTOM</span></code></pre>
        """

        try:
            stop_time = time.perf_counter_ns()  # For precision, this is the first operation of the function.
            controller.stop(self, thread, stop_time)
        except Exception:  # pragma: no cover
            error.message_for_action("when trying to stop the Timer", thread)  # pragma: no cover
