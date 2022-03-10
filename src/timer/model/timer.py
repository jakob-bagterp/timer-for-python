from abc import ABC, abstractmethod

from .. import constant, helper
from .thread_item import ThreadItem


class TimerObject(ABC):
    """Abstract base class of Timer object."""

    _instance = None

    def __new__(cls, decimals: int = constant.decimals.DEFAULT):
        if not cls._instance:  # Singleton: Ensure there's only a single instance of Timer running.
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, decimals: int = constant.decimals.DEFAULT) -> None:
        """Initiates basic properties of the Timer."""

        self.threads: list[ThreadItem] = []
        self.decimals: int = decimals if decimals == constant.decimals.DEFAULT else helper.decimals.validate_and_normalise(
            decimals)

    @abstractmethod
    def start(self, thread: str, decimals: int) -> None:
        """Starts the Timer."""

        raise NotImplementedError

    @abstractmethod
    def stop(self, thread: str) -> None:
        """Stops the Timer."""

        raise NotImplementedError
