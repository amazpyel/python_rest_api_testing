import pytest

from rest_api_client.football_api.client import FootballApiClient


@pytest.fixture
def football_api_client():
    with FootballApiClient() as client:
        yield client
