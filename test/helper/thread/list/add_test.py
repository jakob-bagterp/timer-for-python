import time
from timer import Timer
import timer.constants as constants
import timer.helper.thread as thread
from mock_data_thread_list import thread_item_a, thread_item_b, thread_item_c

class TestAddToThreadList():
    def test_add_to_empty_threads_list(self) -> None:
        timer = Timer()
        assert len(timer.threads) == 0
        thread.list.add(
            timer = timer,
            thread = constants.none_value(),
            start_time = time.perf_counter_ns(),
            decimals = constants.decimals.default())
        assert len(timer.threads) == 1
        thread.list.add(
            timer = timer,
            thread = "TEST",
            start_time = time.perf_counter_ns(),
            decimals = constants.decimals.maximum())
        assert len(timer.threads) == 2
        del timer
    
    def test_added_thread_item_matches_input(self) -> None:
        _thread_item_a = thread_item_a()
        _thread_item_b = thread_item_b()
        _thread_item_c = thread_item_c()
        timer = Timer()
        assert len(timer.threads) == 0
        thread.list.add(
            timer = timer,
            thread = _thread_item_a.name,
            start_time = _thread_item_a.start_time,
            decimals = _thread_item_a.decimals)
        assert len(timer.threads) == 1
        assert timer.threads[0] == _thread_item_a
        assert timer.threads[0] != _thread_item_b
        assert timer.threads[0] != _thread_item_c
        del timer
