import functools
import time

import httpx

from .exceptions import AuthError, NotFoundError, RestApiError, ServerError


def retry(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        for attempt in range(self._max_retries + 1):
            try:
                return func(self, *args, **kwargs)

            except httpx.HTTPStatusError as exc:
                status = exc.response.status_code

                if 500 <= status < 600 and attempt < self._max_retries:
                    time.sleep(self._backoff_factor * (2**attempt))
                    continue

                if status in (401, 403):
                    raise AuthError(f"{status}: {exc.response.text}") from exc
                if status == 404:
                    raise NotFoundError(f"{status}: {exc.response.text}") from exc
                if 500 <= status < 600:
                    raise ServerError(f"{status}: {exc.response.text}") from exc
                raise RestApiError(f"{status}: {exc.response.text}") from exc

            except (httpx.ConnectError, httpx.ReadError, httpx.TimeoutException) as exc:
                if attempt < self._max_retries:
                    time.sleep(self._backoff_factor * (2**attempt))
                    continue

                raise RestApiError(f"Request failed after retries: {exc}") from exc

        raise RestApiError("Request failed after retries")

    return wrapper