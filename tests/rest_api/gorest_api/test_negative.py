import pytest

from src.rest_api_client.exceptions import RestApiError
from src.rest_api_client.go_rest_api.client import GoRestClient


def test_invalid_gorest_token_returns_error(monkeypatch):
    monkeypatch.setenv("GOREST_TOKEN", "invalid_token")

    with GoRestClient() as gorest_client:
        with pytest.raises(RestApiError):
            gorest_client.get_user(1)