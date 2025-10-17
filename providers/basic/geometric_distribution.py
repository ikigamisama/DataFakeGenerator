import numpy as np
from providers.base_provider import BaseProvider


class GeometricDistributionProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, probability: float = 0.5, ** kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)
        self.p = probability

    def generate_non_blank(self):
        return int(np.random.geometric(self.p))
