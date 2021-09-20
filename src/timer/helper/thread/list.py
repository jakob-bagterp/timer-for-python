import constants.list_key
import error

def lookup_index(timer: object, thread: str) -> int:
    try:
        entry_index = None
        entry_counter = 0
        for entry in timer.thread_list:
            if entry.get(constants.list_key.thread()) == thread: # Check if thread already exists in list. Note that this expects a normalised thread (i.e. string and not None) and already in uppercase so it evaluates as intended.
                entry_index = entry_counter
                break # Make sure only the first match is returned, yet the main function is not designed to allow input of duplicates.
            else:
                entry_counter += 1
        return entry_index
    except Exception:
        error.message_for_action(f"in the Timer's lookup module", thread = thread)

def get_start_time_and_decimals(timer: object, entry_index: int) -> tuple[int, int]:
    try:
        entry = timer.thread_list[entry_index]
        start_time = entry.get(constants.list_key.start_time())
        decimals = entry.get(constants.list_key.decimals())
        return start_time, decimals
    except Exception:
        error.message_for_action(f"when trying to look up the Timer values for entry index \"{entry_index}\"")

def add(timer: object, thread, start_time: int, decimals: int) -> None:
    try:
        timer.thread_list.append({
            constants.list_key.thread(): thread,
            constants.list_key.start_time(): start_time,
            constants.list_key.decimals(): decimals
        })
    except Exception:
        error.message_for_action(f"when trying to add entry to the Timer's thread list", thread = thread)

def remove(timer: object, entry_index: int) -> None:
    try:
        timer.thread_list.pop(entry_index)
    except Exception:
        error.message_for_action(f"when trying to remove entry from the Timer's thread list for entry index \"{entry_index}\"")
