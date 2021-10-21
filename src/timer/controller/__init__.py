__all__ = ["start", "stop"]

from .. import error
from .. import helper
from ..helper.time_fractions import TimeFractions
from ..model.timer import TimerObject

def start(timer: TimerObject, thread: str, start_time: int, decimals: int) -> None:
    try:
        thread = helper.thread.normalise_to_string_and_uppercase(thread)
        decimals = helper.decimals.mediate(timer, decimals)
        thread_item, _ = helper.thread.list.try_get_thread_item_and_index(timer, thread)
        if thread_item is None: # If no match in existing threads, create new entry in the thread list.
            helper.thread.list.add(timer, thread, start_time, decimals)
        else:
            error.start_controller(thread)
    except Exception:
        error.message_for_action(f"in the Timer's start thread controller", thread = thread)

def stop(timer: TimerObject, thread: str, stop_time: int) -> None:
    try:
        thread = helper.thread.normalise_to_string_and_uppercase(thread)
        thread_item, entry_index = helper.thread.list.try_get_thread_item_and_index(timer, thread)
        if thread_item is not None: # If there's a match in existing threads, return values to the stop function and remove the entry.
            helper.thread.list.remove(timer, entry_index)
            elapsed_time = stop_time - thread_item.start_time
            time_fractions = TimeFractions(elapsed_time)
            helper.output.message(thread, time_fractions, thread_item.decimals)
        else:
            error.stop_controller(timer, thread)
    except Exception:
        error.message_for_action(f"in the Timer's stop thread controller", thread = thread)
