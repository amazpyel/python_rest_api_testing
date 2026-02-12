import pytest
from src.rest_api_client.client import RestApiClient

@pytest.fixture
def rest_api_client():
    client = RestApiClient()
    yield client
    client.close()
