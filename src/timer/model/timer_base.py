from abc import ABC, abstractmethod

from .thread_item import ThreadItem


class TimerBase(ABC):
    """Abstract base class of Timer object."""

    def __init__(self) -> None:
        self.threads: list[ThreadItem]
        self.decimals: int

    @abstractmethod
    def start(self, thread: str, decimals: int) -> None:
        """Starts the Timer."""

        raise NotImplementedError

    @abstractmethod
    def stop(self, thread: str) -> None:
        """Stops the Timer."""

        raise NotImplementedError