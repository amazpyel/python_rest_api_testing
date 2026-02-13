import logging
import os

import pytest

from src.rest_api_client.football_api.client import FootballApiClient
from src.rest_api_client.gorest_api.client import GoRestClient


@pytest.fixture
def football_api_client():
    with FootballApiClient() as client:
        yield client

@pytest.fixture
def gorest_client():
    with GoRestClient() as client:
        yield client

def pytest_configure():
    logging.basicConfig(
        level=os.getenv("LOG_LEVEL", "WARNING").upper(),
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )