from core.datafake_generator import DataFakeGenerator
from core.exporters import Exporter


schema = [
    {
        "label": "Address Line 2",
        "group": "basic",
        "key_label": "address_line_2",
        "options": {"blank_percentage": 0.1}
    }
]

generator = DataFakeGenerator(schema)
data = generator.generate_many(n=10)

Exporter.to_csv(data, "output/data.csv")
