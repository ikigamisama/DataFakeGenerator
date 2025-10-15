from core.datafake_generator import DataFakeGenerator
from core.exporters import Exporter


schema = [
    {
        "label": "App Bundle ID",
        "group": "it",
        "key_label": "app_bundle_id",
        "options": {"blank_percentage": 0.1}
    },
    {
        "label": "App Name",
        "group": "it",
        "key_label": "app_name",
        "options": {"blank_percentage": 0.1}
    },
    {
        "label": "App Version",
        "group": "it",
        "key_label": "app_version",
        "options": {"blank_percentage": 0.1}
    }
]

generator = DataFakeGenerator(schema)
data = generator.generate_many(n=10)

Exporter.to_csv(data, "output/data.csv")
