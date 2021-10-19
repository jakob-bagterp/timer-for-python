__all__ = ["is_none", "normalise_to_string_and_uppercase", "list"]

from . import list

from ... import constants

def is_none(thread: str) -> bool:
    return True if thread is None or thread == "NONE" else False # NB: Has to be string and upppercase.

def normalise_to_string_and_uppercase(thread: str) -> str: # The thread list iterator only supports strings and numbers and not None, hence the renaming to "NONE".
    return constants.none_value() if is_none(thread) else str(thread).upper()
