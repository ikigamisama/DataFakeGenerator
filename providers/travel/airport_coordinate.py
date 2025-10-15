from providers.base_provider import BaseProvider


class AirportCoordinateProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage,
                         datasets=['airport'], **kwargs)
        self.data = None

    def generate_non_blank(self):
        return self.get_row_data_from_datasets('airport', 'coordinates')
