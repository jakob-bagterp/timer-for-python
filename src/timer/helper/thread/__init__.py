__all__ = ["is_none", "normalise_to_string_and_uppercase", "list"]

from ...constant.various import NONE_VALUE
from . import list


def is_none(thread: str | None) -> bool:
    return thread is None or thread == NONE_VALUE


def normalise_to_string_and_uppercase(thread: str | None) -> str:
    """The thread list iterator only supports strings and numbers and not None, hence the renaming to "NONE"."""

    return NONE_VALUE if is_none(thread) else str(thread).upper()
