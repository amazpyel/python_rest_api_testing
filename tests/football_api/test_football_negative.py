import pytest

from rest_api_client.exceptions import RestApiError
from rest_api_client.football_api.client import FootballApiClient

@pytest.mark.negative
def test_invalid_football_api_token_returns_error(monkeypatch):
    monkeypatch.setenv("FOOTBALL_DATA_TOKEN", "invalid_token")

    with FootballApiClient() as football_client:
        with pytest.raises(RestApiError):
            football_client.get_areas()
