__all__ = ["update_decimals", "start", "stop"]

import error
import helper.decimals
import helper.thread
import helper.thread.list

def start(timer: object, thread: str, start_time: int, decimals: int) -> None:
    try:
        thread = helper.thread.normalise_to_string_and_uppercase(thread)
        decimals = helper.decimals.mediate(timer, decimals)
        entry_index = helper.thread.list.lookup_index(timer, thread)
        if entry_index is None: # If no match in existing threads, create new entry in the thread list.
            helper.thread.list.add(timer, thread, start_time, decimals)
        else:
            error.start_controller(thread)
    except Exception:
        error.message_for_action(f"in the Timer's start thread controller", thread = thread)

def stop(timer: object, thread: str, stop_time: int) -> None:
    try:
        thread = helper.thread.normalise_to_string_and_uppercase(thread)
        entry_index = helper.thread.list.lookup_index(timer, thread)
        if entry_index is not None: # If there's a match in existing threads, return values to the stop function and remove the entry.
            thread_item = helper.thread.list.get_thread_item(timer, entry_index)
            elapsed_time = stop_time - thread_item.start_time
            helper.thread.list.remove(timer, entry_index)
            helper.output_message(thread, elapsed_time, thread_item.decimals)
        else:
            error.stop_controller(timer, thread)
    except Exception:
        error.message_for_action(f"in the Timer's stop thread controller", thread = thread)
