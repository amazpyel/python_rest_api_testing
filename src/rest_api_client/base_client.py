import os

import httpx

from .retry import retry
from .http import HttpMethod


class BaseRestApiClient:
    def __init__(
        self,
        base_url: str,
        headers: dict | None = None,
        timeout: float | None = None,
        max_retries: int = 3,
        backoff_factor: float = 0.5
    ):
        timeout_value = timeout or float(os.getenv("API_TIMEOUT", 10.0))
        self._client = httpx.Client(
            base_url = base_url,
            headers = headers,
            timeout = timeout_value
        )

        self._max_retries = max_retries
        self._backoff_factor = backoff_factor

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @retry
    def _request(self, method: HttpMethod, url: str, **kwargs):
        response = self._client.request(method.value, url, **kwargs)
        response.raise_for_status()
        return response

    def close(self):
        self._client.close()