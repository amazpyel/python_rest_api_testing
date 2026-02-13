import time

import httpx

from .exceptions import RestApiError


def retry(func):
    def wrapper(self, *args, **kwargs):
        for attempt in range(self._max_retries + 1):
            try:
                return func(self, *args, **kwargs)

            except httpx.HTTPStatusError as exc:
                status = exc.response.status_code

                if 500 <= status < 600 and attempt < self._max_retries:
                    time.sleep(self._backoff_factor * (2 ** attempt))
                    continue

                raise RestApiError(f"{status}: {exc.response.text}") from exc

            except (httpx.ConnectError, httpx.ReadError) as exc:
                if attempt < self._max_retries:
                    time.sleep(self._backoff_factor * (2 ** attempt))
                    continue

                raise RestApiError(f"Request failed after retries: {exc}") from exc

        raise RestApiError("Request failed after retries")

    return wrapper