import random
import string
from providers.base_provider import BaseProvider


class BankRiadCodeProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)

    def generate_non_blank(self):
        return "R" + ''.join(random.choices(string.digits, k=8))
