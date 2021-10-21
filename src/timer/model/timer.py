from abc import ABC, abstractmethod

class TimerObject(ABC):
    """Abstract base class of Timer object"""

    @abstractmethod
    def start(self, thread: str, decimals: int) -> None:
        """Starts the Timer"""
    
    @abstractmethod
    def stop(self, thread: str) -> None:
        """Stops the Timer"""
