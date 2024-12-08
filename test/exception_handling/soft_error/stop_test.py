import time
from os import linesep

from colorist import Color

from timer import Timer


def test_timer_stop_unknown_thread_soft_error_1(capfd: object) -> None:
    thread = "custom"

    timer = Timer()
    timer._threads = []
    timer.start()
    time.sleep(0.1)
    timer.stop(thread=thread)
    terminal_output, _ = capfd.readouterr()
    assert terminal_output == rf"{Color.YELLOW}Timer for thread {thread.upper()} is not running. Use .start(thread='{thread.upper()}') to start it.{Color.OFF}{linesep}Or maybe you aren't stopping the right thread? Currently open threads: NONE{linesep}"


def test_timer_stop_unknown_thread_soft_error_2(capfd: object) -> None:
    thread_1 = "custom_1"
    thread_2 = "custom_2"

    timer = Timer()
    timer._threads = []
    timer.start(thread=thread_1)
    time.sleep(0.1)
    timer.stop(thread=thread_2)
    terminal_output, _ = capfd.readouterr()
    assert terminal_output == rf"{Color.YELLOW}Timer for thread {thread_2.upper()} is not running. Use .start(thread='{thread_2.upper()}') to start it.{Color.OFF}{linesep}Or maybe you aren't stopping the right thread? Currently open threads: {thread_1.upper()}{linesep}"


def test_timer_stop_not_started_thread_soft_error_1(capfd: object) -> None:
    timer = Timer()
    timer._threads = []
    timer.stop()
    terminal_output, _ = capfd.readouterr()
    assert terminal_output == f"{Color.YELLOW}Timer is not running. Use .start() to start it.{Color.OFF}{linesep}"


def test_timer_stop_not_started_thread_soft_error_2(capfd: object) -> None:
    thread = "custom"

    timer = Timer()
    timer._threads = []
    timer.stop(thread=thread)
    terminal_output, _ = capfd.readouterr()
    assert terminal_output == f"{Color.YELLOW}Timer for thread {thread.upper()} is not running. Use .start(thread='{thread.upper()}') to start it.{Color.OFF}{linesep}"
