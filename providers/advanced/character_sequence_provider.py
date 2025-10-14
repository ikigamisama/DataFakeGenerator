# providers/advanced/character_sequence_provider.py
from providers.base_provider import BaseProvider
import random
import string


class CharacterSequenceProvider(BaseProvider):
    """
    Generates random sequences of characters, digits, and symbols
    based on a format string that can include wildcard symbols:

    Wildcards:
      # → random digit (0-9)
      @ → random lowercase letter (a-z)
      ^ → random uppercase letter (A-Z)
      * → random digit or letter
      $ → random digit or lowercase letter
      % → random digit or uppercase letter
    """

    def __init__(self, *, format: str = "@@##%", blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)
        self.format = format

    def _random_char(self, symbol: str) -> str:
        """Return a random character based on symbol."""
        if symbol == "#":
            return random.choice(string.digits)
        elif symbol == "@":
            return random.choice(string.ascii_lowercase)
        elif symbol == "^":
            return random.choice(string.ascii_uppercase)
        elif symbol == "*":
            return random.choice(string.ascii_letters + string.digits)
        elif symbol == "$":
            return random.choice(string.ascii_lowercase + string.digits)
        elif symbol == "%":
            return random.choice(string.ascii_uppercase + string.digits)
        else:
            return symbol

    def generate_non_blank(self):
        return "".join(self._random_char(c) for c in self.format)
