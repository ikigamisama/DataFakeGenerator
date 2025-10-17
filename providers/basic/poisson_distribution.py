import numpy as np
from providers.base_provider import BaseProvider


class PoissonDistributionProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, mean: float = 0.0,  ** kwargs):
        super().__init__(blank_percentage=blank_percentage, **kwargs)
        self.mean = mean

    def generate_non_blank(self):
        return int(np.random.poisson(self.mean))
