from core.datafake_generator import DataFakeGenerator
from core.exporters import Exporter


schema = [
    {
        "label": "Base64 Img",
        "key_label": "base64_image",
        "group": 'it',
        "options": {"blank_percentage": 0.1}
    },


]

generator = DataFakeGenerator(schema)
data = generator.generate_many(n=25)

Exporter.to_csv(data, "output/data.csv")
