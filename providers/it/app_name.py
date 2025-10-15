from providers.base_provider import BaseProvider


class AppNameProvider(BaseProvider):
    def __init__(self, blank_percentage: float = 0.0, **kwargs):
        super().__init__(blank_percentage=blank_percentage,
                         datasets=['app'], **kwargs)

    def generate_non_blank(self):
        return self.get_row_data_from_datasets('app', 'app_name')
