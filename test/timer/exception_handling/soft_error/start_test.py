from _constant.terminal import LINESEP
from _helper.random import random_thread_name
from _helper.timer import ensure_all_timer_threads_are_stopped
from colorist import Color

from timer import Timer


def test_timer_start_thread_name_collision_soft_error_without_context_manager(capfd: object) -> None:
    custom_thread = random_thread_name()
    timer = ensure_all_timer_threads_are_stopped()
    timer.start(thread=custom_thread)
    timer.start(thread=custom_thread)
    terminal_output, _ = capfd.readouterr()
    assert (
        terminal_output
        == f"{Color.YELLOW}Timer for thread {custom_thread.upper()} is running. Use .stop(thread='{custom_thread.upper()}') to stop it.{Color.OFF}\n"
    )


def test_timer_start_thread_name_collision_soft_error_with_context_manager(capfd: object) -> None:
    custom_thread = random_thread_name()
    timer = ensure_all_timer_threads_are_stopped()
    timer.start(thread=custom_thread)
    with Timer(thread=custom_thread):
        pass
    terminal_output, _ = capfd.readouterr()
    assert str(terminal_output).startswith(
        f"{Color.YELLOW}Timer for thread {custom_thread.upper()} is running. Use .stop(thread='{custom_thread.upper()}') to stop it.{Color.OFF}{LINESEP}"
        + "Elapsed time:"
    )
    assert str(terminal_output).endswith(f" for thread {Color.GREEN}{custom_thread.upper()}{Color.OFF}\n")


def test_timer_start_default_thread_twice_soft_error_without_context_manager(capfd: object) -> None:
    timer = ensure_all_timer_threads_are_stopped()
    timer.start()
    timer.start()
    terminal_output, _ = capfd.readouterr()
    assert terminal_output == f"{Color.YELLOW}Timer is running. Use .stop() to stop it.{Color.OFF}\n"
