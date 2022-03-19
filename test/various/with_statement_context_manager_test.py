import time

from _constant.interval import ULTRA_SHORT_INTERVAL
from _helper.terminal_output import (verify_decimals_in_terminal_output,
                                     verify_prefix_in_terminal_output)
from _mock_data.decimals import DECIMALS_RANGE

from timer import Timer
from timer.constant.decimals import DEFAULT


def test_with_statement_context_manager(capfd: object) -> None:
    with Timer():
        time.sleep(ULTRA_SHORT_INTERVAL)
    terminal_output, _ = capfd.readouterr()
    assert verify_prefix_in_terminal_output(terminal_output)


def test_with_statement_context_manager_with_thread(capfd: object) -> None:
    _thread = "thread"  # TODO: Use random thread name instead.
    with Timer(thread=_thread):
        time.sleep(ULTRA_SHORT_INTERVAL)
    terminal_output, _ = capfd.readouterr()
    assert verify_prefix_in_terminal_output(terminal_output)
    assert _thread in terminal_output


def test_with_statement_context_manager_with_decimals(capfd: object) -> None:
    for decimals in DECIMALS_RANGE:
        with Timer(decimals=decimals):
            time.sleep(ULTRA_SHORT_INTERVAL)
        terminal_output, _ = capfd.readouterr()
        assert verify_prefix_in_terminal_output(terminal_output)
        assert verify_decimals_in_terminal_output(decimals, terminal_output)


def test_with_statement_context_manager_with_thread_and_decimals(capfd: object) -> None:
    _thread = "thread"  # TODO: Use random thread name instead.
    for decimals in DECIMALS_RANGE:
        with Timer(thread=_thread, decimals=decimals):
            time.sleep(ULTRA_SHORT_INTERVAL)
        terminal_output, _ = capfd.readouterr()
        assert verify_prefix_in_terminal_output(terminal_output)
        assert _thread in terminal_output
        assert verify_decimals_in_terminal_output(decimals, terminal_output)


def test_with_statement_context_manager_with_multiple_nested_threads_and_decimals(capfd: object) -> None:
    _thread_a = "A-LIST"  # TODO: Use random thread name instead.
    _thread_b = "B-LIST"  # TODO: Use random thread name instead.
    for decimals in DECIMALS_RANGE:
        with Timer():
            with Timer(thread=_thread_a, decimals=decimals):
                time.sleep(ULTRA_SHORT_INTERVAL)
                with Timer(thread=_thread_b):
                    time.sleep(ULTRA_SHORT_INTERVAL)
                terminal_output_1, _ = capfd.readouterr()
                assert verify_prefix_in_terminal_output(terminal_output_1)
                assert _thread_b in terminal_output_1
                assert verify_decimals_in_terminal_output(DEFAULT, terminal_output_1)
            terminal_output_2, _ = capfd.readouterr()
            assert verify_prefix_in_terminal_output(terminal_output_2)
            assert _thread_a in terminal_output_2
            assert verify_decimals_in_terminal_output(decimals, terminal_output_2)
        terminal_output_3, _ = capfd.readouterr()
        assert verify_prefix_in_terminal_output(terminal_output_3)


def test_mix_of_context_manager_standard(capfd: object) -> None:
    _thread = "thread"  # TODO: Use random thread name instead + None type.
    timer = Timer()
    timer.start(thread=_thread)
    with Timer():
        time.sleep(ULTRA_SHORT_INTERVAL)
    terminal_output_1, _ = capfd.readouterr()
    assert verify_prefix_in_terminal_output(terminal_output_1)
    timer.stop(_thread)
    terminal_output_2, _ = capfd.readouterr()
    assert _thread in terminal_output_2
    assert verify_prefix_in_terminal_output(terminal_output_2)
