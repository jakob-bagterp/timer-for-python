import time
from os import linesep

import pytest
from _constant.interval import ULTRA_SHORT_INTERVAL
from _helper import operating_system
from _helper.random import random_thread_name, random_thread_name_but_not
from _helper.timer import ensure_all_timer_threads_are_stopped
from colorist import Color


def test_timer_stop_unknown_thread_soft_error_with_default_and_custom_thread(capfd: object) -> None:
    if operating_system.is_windows():
        pytest.skip("Skipping test for Windows due to line separator issue.")  # pragma: no cover
        # TODO: Fix line separator issue on Windows.
        return  # pragma: no cover

    custom_thread = random_thread_name()
    timer = ensure_all_timer_threads_are_stopped()
    timer.start()
    time.sleep(ULTRA_SHORT_INTERVAL)
    timer.stop(thread=custom_thread)
    terminal_output, _ = capfd.readouterr()
    assert terminal_output == \
        f"{Color.YELLOW}Timer for thread {custom_thread.upper()} is not running. Use .start(thread='{custom_thread.upper()}') to start it.{Color.OFF}{linesep}" +\
        f"Or maybe you aren't stopping the right thread? Currently open threads: NONE{linesep}"


def test_timer_stop_unknown_thread_soft_error_with_multiple_custom_threads(capfd: object) -> None:
    if operating_system.is_windows():
        pytest.skip("Skipping test for Windows due to line separator issue.")  # pragma: no cover
        # TODO: Fix line separator issue on Windows.
        return  # pragma: no cover

    custom_thread_1 = random_thread_name()
    custom_thread_2 = random_thread_name_but_not(custom_thread_1)
    timer = ensure_all_timer_threads_are_stopped()
    timer.start(thread=custom_thread_1)
    time.sleep(ULTRA_SHORT_INTERVAL)
    timer.stop(thread=custom_thread_2)
    terminal_output, _ = capfd.readouterr()
    assert terminal_output == \
        f"{Color.YELLOW}Timer for thread {custom_thread_2.upper()} is not running. Use .start(thread='{custom_thread_2.upper()}') to start it.{Color.OFF}{linesep}" +\
        f"Or maybe you aren't stopping the right thread? Currently open threads: {custom_thread_1.upper()}{linesep}"


def test_timer_stop_not_started_thread_soft_error_without_start(capfd: object) -> None:
    timer = ensure_all_timer_threads_are_stopped()
    timer.stop()
    terminal_output, _ = capfd.readouterr()
    assert terminal_output == f"{Color.YELLOW}Timer is not running. Use .start() to start it.{Color.OFF}\n"


def test_timer_stop_not_started_thread_soft_error_without_start_and_with_custom_thread(capfd: object) -> None:
    custom_thread = random_thread_name()
    timer = ensure_all_timer_threads_are_stopped()
    timer.stop(thread=custom_thread)
    terminal_output, _ = capfd.readouterr()
    assert terminal_output == f"{Color.YELLOW}Timer for thread {custom_thread.upper()} is not running. Use .start(thread='{custom_thread.upper()}') to start it.{Color.OFF}\n"


def test_timer_stop_default_thread_while_custom_thread_is_running_soft_error(capfd: object) -> None:
    if operating_system.is_windows():
        pytest.skip("Skipping test for Windows due to line separator issue.")  # pragma: no cover
        # TODO: Fix line separator issue on Windows.
        return  # pragma: no cover

    custom_thread = random_thread_name()
    timer = ensure_all_timer_threads_are_stopped()
    timer.start(thread=custom_thread)
    timer.stop()
    terminal_output, _ = capfd.readouterr()
    assert terminal_output ==  \
        f"{Color.YELLOW}Timer is not running. Use .start() to start it.{Color.OFF}{linesep}" +\
        f"Or maybe you aren't stopping the right thread? Currently open threads: {custom_thread.upper()}{linesep}"
