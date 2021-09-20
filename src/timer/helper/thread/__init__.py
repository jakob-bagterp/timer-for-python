__all__ = ["is_none"]

def is_none(thread: str) -> bool:
    return True if thread == None or thread == "NONE" else False # NB: Has to be string and upppercase.
