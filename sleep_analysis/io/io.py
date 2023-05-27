from pathlib import Path
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sleep_analysis.model import DataModel

class IO(ABC):
    """Metaclass for I/O classes"""

    @abstractmethod
    def load(self, path:Path) -> DataModel:
        """Load some path and return some datamodel or a child class"""
