import time

from _helper.terminal_output import verify_decimals_in_terminal_output
from _mock_data.decimals import DECIMALS_RANGE

from timer import Timer

SHORT_INTERVAL: float = 0.01  # Seconds.

EXPECTED_TERMINAL_OUTPUT_PREFIX: str = "Elapsed time"


def test_with_statement_context_manager(capfd: object) -> None:
    with Timer():
        time.sleep(SHORT_INTERVAL)
    terminal_output, _ = capfd.readouterr()
    assert EXPECTED_TERMINAL_OUTPUT_PREFIX in terminal_output


def test_with_statement_context_manager_with_thread(capfd: object) -> None:
    _thread = "thread"  # TODO: Use random thread name instead.
    with Timer(thread=_thread):
        time.sleep(SHORT_INTERVAL)
    terminal_output, _ = capfd.readouterr()
    assert EXPECTED_TERMINAL_OUTPUT_PREFIX in terminal_output
    assert _thread in terminal_output


def test_with_statement_context_manager_with_decimals(capfd: object) -> None:
    for decimals in DECIMALS_RANGE:
        with Timer(decimals=decimals):
            time.sleep(SHORT_INTERVAL)
        terminal_output, _ = capfd.readouterr()
        assert EXPECTED_TERMINAL_OUTPUT_PREFIX in terminal_output
        assert verify_decimals_in_terminal_output(decimals, terminal_output)


def test_with_statement_context_manager_with_thread_and_decimals(capfd: object) -> None:
    _thread = "thread"  # TODO: Use random thread name instead.
    for decimals in DECIMALS_RANGE:
        with Timer(thread=_thread, decimals=decimals):
            time.sleep(SHORT_INTERVAL)
        terminal_output, _ = capfd.readouterr()
        assert EXPECTED_TERMINAL_OUTPUT_PREFIX in terminal_output
        assert _thread in terminal_output
        assert verify_decimals_in_terminal_output(decimals, terminal_output)
