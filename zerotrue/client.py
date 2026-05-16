"""Main ZeroTrue client."""

from zerotrue.http_client import HTTPClient
from zerotrue.resources.checks import Checks


class ZeroTrue:
    """Main client for ZeroTrue API."""

    def __init__(
        self,
        api_key: str,
        timeout: int = 30000,
        max_retries: int = 3,
        retry_delay: int = 1000,
        debug: bool = False,
    ):
        """
        Initialize ZeroTrue client.

        Args:
            api_key: Your ZeroTrue API key
            timeout: Request timeout in milliseconds (default: 30000)
            max_retries: Max retry attempts (default: 3)
            retry_delay: Delay between retries in milliseconds (default: 1000)
            debug: Enable debug logging (default: False)
        """
        if not api_key:
            raise ValueError("api_key is required")

        self._http_client = HTTPClient(
            api_key=api_key,
            timeout=timeout,
            max_retries=max_retries,
            retry_delay=retry_delay,
            debug=debug,
        )
        self.checks = Checks(self._http_client)
