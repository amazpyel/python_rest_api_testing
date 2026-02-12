import pytest

from src.rest_api_client.client import RestApiClient, RestApiError


def test_invalid_token_returns_error(monkeypatch):
    monkeypatch.setenv("FOOTBALL_DATA_TOKEN", "invalid_token")

    client = RestApiClient()
    with pytest.raises(RestApiError):
        client.get_areas()

    client.close()