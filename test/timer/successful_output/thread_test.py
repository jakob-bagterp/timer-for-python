import re
import time

from _constant.interval import ONE_MILLISECOND_AS_SECOND
from _helper.random import random_thread_name
from _helper.terminal_output import successful_output_regex
from _helper.timer import ensure_all_timer_threads_are_stopped

from timer import Timer


def test_timer_thread_output(capfd: object) -> None:
    ensure_all_timer_threads_are_stopped()
    custom_thread = random_thread_name()
    with Timer(thread=custom_thread):
        time.sleep(ONE_MILLISECOND_AS_SECOND)
    terminal_output, _ = capfd.readouterr()
    expected_output_regex = successful_output_regex(thread=custom_thread)
    assert re.fullmatch(expected_output_regex, terminal_output)
