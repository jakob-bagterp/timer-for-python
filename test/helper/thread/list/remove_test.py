from timer import Timer
import timer.helper.thread as thread
from mock_data.thread_list import thread_item_default, thread_item_a, thread_item_b, thread_item_c, generate_timer_with_threads_list

class TestRemoveFromThreadList():
    def test_remove_items_from_threads_list(self) -> None:
        timer = generate_timer_with_threads_list()
        assert len(timer.threads) == 4
        thread.list.remove(timer, 0)
        assert len(timer.threads) == 3
        thread.list.remove(timer, 2)
        assert len(timer.threads) == 2
        thread.list.remove(timer, 1)
        assert len(timer.threads) == 1
        thread.list.remove(timer, 0)
        assert len(timer.threads) == 0
        del timer
    
    def test_removed_item_from_threads_list_matches_remaining_items(self) -> None:
        timer = Timer()
        assert len(timer.threads) == 0
        _thread_item_default = thread_item_default()
        _thread_item_a = thread_item_a()
        _thread_item_b = thread_item_b()
        _thread_item_c = thread_item_c()
        timer.threads = [
            _thread_item_default,
            _thread_item_a,
            _thread_item_b,
            _thread_item_c]
        assert len(timer.threads) == 4
        assert timer.threads[0] == _thread_item_default
        assert timer.threads[1] == _thread_item_a
        assert timer.threads[2] == _thread_item_b
        assert timer.threads[3] == _thread_item_c
        thread.list.remove(timer, 0)
        assert len(timer.threads) == 3
        assert timer.threads[0] == _thread_item_a
        assert timer.threads[1] == _thread_item_b
        assert timer.threads[2] == _thread_item_c
        thread.list.remove(timer, 1)
        assert len(timer.threads) == 2
        assert timer.threads[0] == _thread_item_a
        assert timer.threads[1] == _thread_item_c
        thread.list.remove(timer, 0)
        assert len(timer.threads) == 1
        assert timer.threads[0] == _thread_item_c
        thread.list.remove(timer, 0)
        assert len(timer.threads) == 0
        del timer
