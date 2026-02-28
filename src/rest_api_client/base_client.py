import logging
import os
import time

import httpx

from .http import HttpMethod
from .retry import retry


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
        self._logger = logging.getLogger(self.__class__.__name__)
        self._client = httpx.Client(
            base_url=base_url,
            headers=headers,
            timeout=timeout_value,
            event_hooks={
                "request": [self._log_request],
                "response": [self._log_response],
            }
        )

        self._max_retries = max_retries
        self._backoff_factor = backoff_factor

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @retry
    def _request(self, method: HttpMethod, url: str, **kwargs):
        response = self._client.request(method, url, **kwargs)
        response.raise_for_status()
        return response

    def close(self):
        self._client.close()

    def _log_request(self, request: httpx.Request):
        # Store start time in request object
        request.extensions["start_time"] = time.perf_counter()

        self._logger.info(
            f"{request.method} {request.url}"
        )

    def _log_response(self, response: httpx.Response):
        start_time = response.request.extensions.get("start_time")

        duration = None
        if start_time is not None:
            duration = time.perf_counter() - start_time

        if duration is not None:
            self._logger.info(
                f"{response.request.method} {response.request.url} "
                f"-> {response.status_code} "
                f"({duration:.3f}s)"
            )
        else:
            self._logger.info(
                f"{response.request.method} {response.request.url} "
                f"-> {response.status_code}"
            )
