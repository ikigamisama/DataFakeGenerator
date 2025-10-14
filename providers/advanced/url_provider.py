import random
from urllib.parse import urlencode
from providers.base_provider import BaseProvider


class UrlProvider(BaseProvider):
    def __init__(
        self,
        *,
        protocol: bool = True,
        host: bool = True,
        path: bool = True,
        query_string: bool = True,
        blank_percentage: float = 0.0,
        **kwargs
    ):
        """
        Generate realistic URLs with optional parts.
        Example formats:
          https://facebook.com/foo/bar?x=1
          http://example.org
          /foo/bar
        """
        super().__init__(blank_percentage=blank_percentage, **kwargs)
        self.protocol_enabled = protocol
        self.host_enabled = host
        self.path_enabled = path
        self.query_enabled = query_string

        self.protocols = ["http", "https"]
        self.hosts = [
            "google.com", "facebook.com", "twitter.com", "github.com",
            "example.org", "mywebsite.net", "openai.com"
        ]
        self.paths = [
            "/", "/home", "/profile", "/search", "/login",
            "/products", "/blog", "/docs", "/foo/bar", "/api/v1/resource"
        ]
        self.query_params = [
            {"foo": "bar"},
            {"id": "123"},
            {"q": "test"},
            {"lang": "en"},
            {"page": "1"},
            {"ref": "newsletter"}
        ]

    def generate_non_blank(self):
        parts = []

        # Protocol
        if self.protocol_enabled:
            protocol = random.choice(self.protocols)
        else:
            protocol = None

        # Host
        if self.host_enabled:
            host = random.choice(self.hosts)
        else:
            host = None

        # Path
        path = random.choice(self.paths) if self.path_enabled else ""

        # Query
        query = ""
        if self.query_enabled and random.random() < 0.5:  # optional
            params = random.choice(self.query_params)
            query = "?" + urlencode(params)

        # Construct URL
        if protocol and host:
            base = f"{protocol}://{host}"
        elif host:
            base = host
        elif protocol:
            base = f"{protocol}://"
        else:
            base = ""

        url = base + path + query
        return url or None
