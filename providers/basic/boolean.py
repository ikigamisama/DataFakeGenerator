import random
from providers.base_provider import BaseProvider


class BooleanProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)

    def generate_non_blank(self):
        return random.choice([True, False])
