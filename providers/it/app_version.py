import random
import string
from providers.base_provider import BaseProvider


class AppVersionProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage,
                         datasets=['airport'], **kwargs)

    def _replace_string(self, char: str) -> str:
        if char == '#':
            return random.choice(string.digits)

        return char

    def generate_non_blank(self):
        num_choice_format = random.choice(['#.##', '#.#.#'])

        return "".join(self._replace_string(f) for f in num_choice_format)
