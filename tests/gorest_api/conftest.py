import pytest

from rest_api_client.gorest_api.client import GoRestClient


@pytest.fixture
def gorest_client():
    with GoRestClient() as client:
        yield client
