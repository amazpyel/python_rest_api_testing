class RestApiError(Exception):
    """Raised when an API request fails."""


class AuthError(RestApiError):
    """Raised on 401/403 responses."""


class NotFoundError(RestApiError):
    """Raised on 404 responses."""


class ServerError(RestApiError):
    """Raised on 5xx responses."""