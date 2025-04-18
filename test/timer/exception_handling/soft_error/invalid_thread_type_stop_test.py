from _constant.terminal import LINESEP
from _helper.random import random_thread_name
from _helper.timer import get_timer_with_invalid_thread_type
from colorist import Color

from timer import Timer


def test_timer_stop_invalid_thread_type_soft_error_without_context_manager(capfd: object) -> None:
    custom_thread = random_thread_name()
    timer = get_timer_with_invalid_thread_type(custom_thread)
    timer.stop(thread=custom_thread)
    terminal_output, _ = capfd.readouterr()
    assert terminal_output == \
        f"{Color.YELLOW}Timer: Something went wrong in the Timer's lookup module for thread {custom_thread.upper()}.{Color.OFF}{LINESEP}" +\
        f"{Color.YELLOW}Timer for thread {custom_thread.upper()} is not running. Use .start(thread='{custom_thread.upper()}') to start it.{Color.OFF}{LINESEP}" +\
        f"{Color.YELLOW}Timer: Something went wrong in the Timer's stop thread controller for thread {custom_thread.upper()}.{Color.OFF}{LINESEP}"


def test_timer_stop_invalid_thread_type_soft_error_with_context_manager(capfd: object) -> None:
    custom_thread = random_thread_name()
    get_timer_with_invalid_thread_type(custom_thread)
    with Timer(thread=custom_thread):
        pass
    terminal_output, _ = capfd.readouterr()
    assert terminal_output == \
        f"{Color.YELLOW}Timer: Something went wrong in the Timer's lookup module for thread {custom_thread.upper()}.{Color.OFF}{LINESEP}" +\
        f"{Color.YELLOW}Timer: Something went wrong in the Timer's lookup module for thread {custom_thread.upper()}.{Color.OFF}{LINESEP}" +\
        f"{Color.YELLOW}Timer for thread {custom_thread.upper()} is not running. Use .start(thread='{custom_thread.upper()}') to start it.{Color.OFF}{LINESEP}" +\
        f"{Color.YELLOW}Timer: Something went wrong in the Timer's stop thread controller for thread {custom_thread.upper()}.{Color.OFF}{LINESEP}"
