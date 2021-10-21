from ... import error
from ...model.thread_item import ThreadItem
from ...model.timer import TimerObject

def try_get_thread_item_and_index(timer: TimerObject, thread: str) -> tuple[ThreadItem, int]:
    try:
        index_counter = 0
        for thread_item in timer.threads:
            if thread_item.name == thread: # Check if thread already exists in list. Note that this expects a normalised thread (i.e. string and not None) and already in uppercase so it evaluates as intended.
                return thread_item, index_counter # Make sure only the first match is returned, yet the main function is not designed to allow input of duplicates.
            else:
                index_counter += 1
        return None, None
    except Exception:
        error.message_for_action(f"in the Timer's lookup module", thread = thread)

def add(timer: TimerObject, thread: str, start_time: int, decimals: int) -> None:
    try:
        timer.threads.append(ThreadItem(name = thread, start_time = start_time, decimals = decimals))
    except Exception:
        error.message_for_action(f"when trying to add entry to the Timer's thread list", thread = thread)

def remove(timer: TimerObject, entry_index: int) -> None:
    try:
        timer.threads.pop(entry_index)
    except Exception:
        error.message_for_action(f"when trying to remove entry from the Timer's thread list for entry index \"{entry_index}\"")
