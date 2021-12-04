__all__ = ["is_none", "normalise_to_string_and_uppercase", "list"]

from . import list

from ...constants import none_value

def is_none(thread: str) -> bool:
    return True if thread is None or thread == none_value() else False

def normalise_to_string_and_uppercase(thread: str) -> str: # The thread list iterator only supports strings and numbers and not None, hence the renaming to "NONE".
    return none_value() if is_none(thread) else str(thread).upper()
