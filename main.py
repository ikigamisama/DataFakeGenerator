from core.datafake_generator import DataFakeGenerator
from core.exporters import Exporter


schema = [
    {
        "label": "Airport Code",
        "group": "travel",
        "key_label": "airport_code",
        "options": {"blank_percentage": 0.1}
    },
    {
        "label": "",
        "group": "travel",
        "key_label": "airport_municipality",
        "options": {"blank_percentage": 0.1}
    },
    {
        "label": "",
        "group": "travel",
        "key_label": "airport_region_code",
        "options": {"blank_percentage": 0.1}
    }
]

generator = DataFakeGenerator(schema)
data = generator.generate_many(n=10)

Exporter.to_csv(data, "output/data.csv")
