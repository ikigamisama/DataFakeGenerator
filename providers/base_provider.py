from abc import ABC, abstractmethod
from core.dataset_manager import DatasetManager


class BaseProvider(ABC):
    def __init__(self, *, blank_percentage: float = 0.0, datasets: list[str] | None = None, **kwargs):
        self.blank_percentage = float(blank_percentage or 0.0)
        self.datasets = datasets or []

    @abstractmethod
    def generate_non_blank(self):
        """Return a non-blank value (providers never handle blanks themselves)."""
        raise NotImplementedError

    def import_datasets(self):
        return {name: DatasetManager.load(name) for name in self.datasets}
