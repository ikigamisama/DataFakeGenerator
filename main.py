from core.datafake_generator import DataFakeGenerator
from core.exporters import Exporter


schema = [
    {
        "label": "Bitcoin Address",
        "key_label": "bitcoin_address",
        "group": 'crypto',
        "options": {"blank_percentage": 0.1}
    },
    {
        "label": "Binomial Distribution",
        "key_label": "binomial_distribution",
        "group": 'basic',
        "options": {"blank_percentage": 0.1, 'probability': 0.5}
    },
    {
        "label": "Exponential Distribution",
        "key_label": "exponential_distribution",
        "group": 'basic',
        "options": {"blank_percentage": 0.1, 'lam': 1}
    },
    {
        "label": "Geometric Distribution",
        "key_label": "geometric_distribution",
        "group": 'basic',
        "options": {"blank_percentage": 0.1, 'probability': 0.5}
    },
    {
        "label": "Normal Distribution",
        "key_label": "normal_distribution",
        "group": 'basic',
        "options": {"blank_percentage": 0.1, 'mean': 0, 'std_dev': 1, 'decimals': 2}
    },
    {
        "label": "Poisson Distribution",
        "key_label": "poisson_distribution",
        "group": 'basic',
        "options": {"blank_percentage": 0.1, 'mean': 0.5}
    },
]

generator = DataFakeGenerator(schema)
data = generator.generate_many(n=100)

Exporter.to_csv(data, "output/data.csv")
Exporter.to_json(data, "output/data.json")
