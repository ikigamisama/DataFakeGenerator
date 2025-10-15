import random
from providers.base_provider import BaseProvider


class AirportCodeProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage,
                         datasets=['airport'], **kwargs)
        self.data = None

    def generate_non_blank(self):
        if self.data is None:
            datasets = self.import_datasets()
            self.data = list({d.get('iata_code')
                             for d in datasets["airport"] if d.get('iata_code')})
        return random.choice(self.data)
