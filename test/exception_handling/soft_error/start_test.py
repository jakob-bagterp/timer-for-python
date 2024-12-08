from _helper.timer import ensure_all_timer_threads_are_stopped
from colorist import Color


def test_timer_start_invalid_thread_type_soft_error_1(capfd: object) -> None:
    custom_thread = "custom"

    timer = ensure_all_timer_threads_are_stopped()
    timer._threads = [custom_thread]  # Should be a list[ThreadItem] type.
    timer.start(thread=custom_thread)
    terminal_output, _ = capfd.readouterr()
    assert terminal_output == f"{Color.YELLOW}Timer: Something went wrong in the Timer's lookup module for thread {custom_thread.upper()}.{Color.OFF}\n"
