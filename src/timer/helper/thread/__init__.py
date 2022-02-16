__all__ = ["is_none", "normalise_to_string_and_uppercase", "list"]

from . import list
from ...constants import none_value

def is_none(thread: str | None) -> bool:
    return thread is None or thread == none_value()

def normalise_to_string_and_uppercase(thread: str | None) -> str: # The thread list iterator only supports strings and numbers and not None, hence the renaming to "NONE".
    return none_value() if is_none(thread) else str(thread).upper()
