from abc import ABC, abstractmethod


class BaseProvider(ABC):
    def __init__(self, *, blank_percentage: float = 0.0, **kwargs):
        self.blank_percentage = float(blank_percentage or 0.0)

    @abstractmethod
    def generate_non_blank(self):
        """Return a non-blank value (providers never handle blanks themselves)."""
        raise NotImplementedError
