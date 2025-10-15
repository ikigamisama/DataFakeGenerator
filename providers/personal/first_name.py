import random
from providers.base_provider import BaseProvider


class FirstNameProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)
        self.names = [
            "Alice", "Bob", "Charlie", "Diana",
            "Ethan", "Fiona", "George", "Hannah",
            "Ian", "Jasmine", "Kyle", "Laura",
            "Mason", "Nina", "Oscar", "Paula",
            "Quinn", "Riley", "Sophia", "Tristan",
            "Uma", "Victor", "Willow", "Xander",
            "Yara", "Zane"
        ]

    def generate_non_blank(self):
        return random.choice(self.names)
