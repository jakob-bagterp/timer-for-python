import time

from _mock_data.thread_list import thread_item_a, thread_item_b, thread_item_c

import timer.constant as constant
import timer.helper.thread as thread
from timer import Timer


def test_add_to_empty_threads_list() -> None:
    timer = Timer()
    timer.threads = []
    assert not timer.threads
    thread.list.add(
        timer=timer,
        thread=constant.various.NONE_VALUE,
        start_time=time.perf_counter_ns(),
        decimals=constant.decimals.DEFAULT
    )
    assert len(timer.threads) == 1
    thread.list.add(
        timer=timer,
        thread="TEST",
        start_time=time.perf_counter_ns(),
        decimals=constant.decimals.MAXIMUM
    )
    assert len(timer.threads) == 2
    del timer


def test_added_thread_item_matches_input() -> None:
    _thread_item_a = thread_item_a()
    _thread_item_b = thread_item_b()
    _thread_item_c = thread_item_c()
    timer = Timer()
    timer.threads = []
    assert not timer.threads
    thread.list.add(
        timer=timer,
        thread=_thread_item_a.name,
        start_time=_thread_item_a.start_time,
        decimals=_thread_item_a.decimals
    )
    assert len(timer.threads) == 1
    assert timer.threads[0] == _thread_item_a
    assert timer.threads[0] != _thread_item_b
    assert timer.threads[0] != _thread_item_c
    del timer
