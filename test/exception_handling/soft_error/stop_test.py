import time
from os import linesep

import pytest
from _helper import operating_system
from _helper.timer import ensure_all_timer_threads_are_stopped
from colorist import Color

from timer import Timer


def test_timer_stop_unknown_thread_soft_error_1(capfd: object) -> None:
    if operating_system.is_windows():
        pytest.skip("Skipping test for Windows due to line separator issue.")  # pragma: no cover
        # TODO: Fix line separator issue on Windows.
        return  # pragma: no cover

    custom_thread = "custom"

    timer = ensure_all_timer_threads_are_stopped()
    timer.start()
    time.sleep(0.1)
    timer.stop(thread=custom_thread)
    terminal_output, _ = capfd.readouterr()
    assert terminal_output == \
        f"{Color.YELLOW}Timer for thread {custom_thread.upper()} is not running. Use .start(thread='{custom_thread.upper()}') to start it.{Color.OFF}{linesep}" +\
        f"Or maybe you aren't stopping the right thread? Currently open threads: NONE{linesep}"


def test_timer_stop_unknown_thread_soft_error_2(capfd: object) -> None:
    if operating_system.is_windows():
        pytest.skip("Skipping test for Windows due to line separator issue.")  # pragma: no cover
        # TODO: Fix line separator issue on Windows.
        return  # pragma: no cover

    custom_thread_1 = "custom_1"
    custom_thread_2 = "custom_2"

    timer = ensure_all_timer_threads_are_stopped()
    timer.start(thread=custom_thread_1)
    time.sleep(0.1)
    timer.stop(thread=custom_thread_2)
    terminal_output, _ = capfd.readouterr()
    assert terminal_output == \
        f"{Color.YELLOW}Timer for thread {custom_thread_2.upper()} is not running. Use .start(thread='{custom_thread_2.upper()}') to start it.{Color.OFF}{linesep}" +\
        f"Or maybe you aren't stopping the right thread? Currently open threads: {custom_thread_1.upper()}{linesep}"


def test_timer_stop_not_started_thread_soft_error_1(capfd: object) -> None:
    timer = ensure_all_timer_threads_are_stopped()
    timer.stop()
    terminal_output, _ = capfd.readouterr()
    assert terminal_output == f"{Color.YELLOW}Timer is not running. Use .start() to start it.{Color.OFF}\n"


def test_timer_stop_not_started_thread_soft_error_2(capfd: object) -> None:
    custom_thread = "custom"

    timer = ensure_all_timer_threads_are_stopped()
    timer.stop(thread=custom_thread)
    terminal_output, _ = capfd.readouterr()
    assert terminal_output == f"{Color.YELLOW}Timer for thread {custom_thread.upper()} is not running. Use .start(thread='{custom_thread.upper()}') to start it.{Color.OFF}\n"


def test_timer_stop_invalid_thread_type_soft_error_1(capfd: object) -> None:
    if operating_system.is_windows():
        pytest.skip("Skipping test for Windows due to line separator issue.")  # pragma: no cover
        # TODO: Fix line separator issue on Windows.
        return  # pragma: no cover

    custom_thread = "custom"

    timer = ensure_all_timer_threads_are_stopped()
    timer._threads = [custom_thread]  # Triggers issue by invalid type as it should be a list[ThreadItem] type.
    timer.stop(thread=custom_thread)
    terminal_output, _ = capfd.readouterr()
    assert terminal_output == \
        f"{Color.YELLOW}Timer: Something went wrong in the Timer's lookup module for thread {custom_thread.upper()}.{Color.OFF}{linesep}" +\
        f"{Color.YELLOW}Timer for thread {custom_thread.upper()} is not running. Use .start(thread='{custom_thread.upper()}') to start it.{Color.OFF}{linesep}" +\
        f"{Color.YELLOW}Timer: Something went wrong in the Timer's stop thread controller for thread {custom_thread.upper()}.{Color.OFF}{linesep}"


def test_timer_stop_invalid_thread_type_soft_error_2(capfd: object) -> None:
    if operating_system.is_windows():
        pytest.skip("Skipping test for Windows due to line separator issue.")  # pragma: no cover
        # TODO: Fix line separator issue on Windows.
        return  # pragma: no cover

    custom_thread = "custom"

    timer = ensure_all_timer_threads_are_stopped()
    timer._threads = [custom_thread]  # Triggers issue by invalid type as it should be a list[ThreadItem] type.
    with Timer(thread=custom_thread):
        pass
    terminal_output, _ = capfd.readouterr()
    assert terminal_output == \
        f"{Color.YELLOW}Timer: Something went wrong in the Timer's lookup module for thread {custom_thread.upper()}.{Color.OFF}{linesep}" +\
        f"{Color.YELLOW}Timer: Something went wrong in the Timer's lookup module for thread {custom_thread.upper()}.{Color.OFF}{linesep}" +\
        f"{Color.YELLOW}Timer for thread {custom_thread.upper()} is not running. Use .start(thread='{custom_thread.upper()}') to start it.{Color.OFF}{linesep}" +\
        f"{Color.YELLOW}Timer: Something went wrong in the Timer's stop thread controller for thread {custom_thread.upper()}.{Color.OFF}{linesep}"
