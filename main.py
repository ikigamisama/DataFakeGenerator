from core.datafake_generator import DataFakeGenerator
from core.exporters import Exporter


schema = [
    {
        "label": "Catch Praise",
        "key_label": "catch_praise",
        "group": 'personal',
        "options": {"blank_percentage": 0.1}
    },
]

generator = DataFakeGenerator(schema)
data = generator.generate_many(n=100)

Exporter.to_csv(data, "output/data.csv")
Exporter.to_json(data, "output/data.json")
