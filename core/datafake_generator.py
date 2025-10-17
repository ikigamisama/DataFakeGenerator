from factory.provider_factory import ProviderFactory
from typing import List, Dict, Any
import random


class DataFakeGenerator:

    def __init__(self, schema: List[Dict[str, Any]]):
        """
        Schema: Format in array of dicts describing each column.

        Example:
        [
            {
                "label": "First Name",
                "group": "personal",
                "key_label": "first_name",
                "options": {"blank_percentage": 0.1}
            },
            {
                "label": "Character Sequence",
                "group": "advanced",
                "key_label": "character_sequence",
                "options": {"format": "@@##", "blank_percentage": 0.05}
            }
        ]
        """

        self.schema = schema
        self.providers = self._initialize_providers()

    def generate_many(self, n: int):
        rows = [{} for _ in range(n)]

        for key, provider in self.providers.items():
            pct = getattr(provider, "blank_percentage", 0.0) or 0.0
            num_blanks = round(n * pct)
            blank_indices = set(random.sample(
                range(n), num_blanks)) if num_blanks > 0 else set()

            for i in range(n):
                if i in blank_indices:
                    rows[i][key] = None
                else:
                    rows[i][key] = provider.generate_non_blank()

        return rows

    def _initialize_providers(self):
        providers = {}
        for col in self.schema:
            key = col["label"]
            group = col["group"]
            label = col["key_label"]
            options = col.get("options", {})
            provider = ProviderFactory.create(
                group=group, label=label, **options)
            providers[key] = provider
        return providers
