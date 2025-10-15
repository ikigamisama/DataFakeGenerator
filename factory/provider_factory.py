import importlib


class ProviderFactory:
    _cache = {}

    @staticmethod
    def create(group: str, label: str, **kwargs):
        """
        Dynamically load and instantiate a provider class.
        File path: providers/{group}/{label}_provider.py
        Class name: {LabelCapitalized}Provider
        """
        module_path = f"providers.{group}.{label.lower()}"
        class_name = "".join(word.capitalize()
                             for word in label.split("_")) + "Provider"
        cache_key = (group, label)

        if cache_key in ProviderFactory._cache:
            provider_class = ProviderFactory._cache[cache_key]
        else:
            module = importlib.import_module(module_path)
            provider_class = getattr(module, class_name)
            ProviderFactory._cache[cache_key] = provider_class

        return provider_class(**kwargs)
