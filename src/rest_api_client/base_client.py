import os

import httpx

from .exceptions import RestApiError
from .http import HttpMethod


class BaseRestApiClient:
    def __init__(self, base_url: str, headers: dict | None = None, timeout: float | None = None):
        timeout_value = timeout or float(os.getenv("API_TIMEOUT", 10.0))
        self._client = httpx.Client(
            base_url = base_url,
            headers = headers,
            timeout = timeout_value
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def _request(self, method: HttpMethod, url: str, **kwargs):
        try:
            response = self._client.request(method.value, url, **kwargs)
            response.raise_for_status()
            return response
        except httpx.HTTPStatusError as exc:
            raise RestApiError(
                f"{method.value} {url} failed with "
                f"{exc.response.status_code}: {exc.response.text}"
            ) from exc


    def close(self):
        self._client.close()