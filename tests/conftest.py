import logging
import os
import platform
import sys
from pathlib import Path

import pytest

from rest_api_client.football_api.client import FootballApiClient
from rest_api_client.gorest_api.client import GoRestClient


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

def pytest_sessionstart(session):
    """
    Generate Allure environment metadata and executor files.
    """
    import json

    results_dir = Path("allure-results")
    results_dir.mkdir(exist_ok=True)

    # Environment properties
    environment_file = results_dir / "environment.properties"
    football_base = os.getenv("FOOTBALL_BASE_URL", "https://api.football-data.org/v4")
    gorest_base = os.getenv("GOREST_BASE_URL", "https://gorest.co.in/public/v2")

    with environment_file.open("w", encoding="utf-8") as f:
        f.write(f"Python Version={sys.version.split()[0]}\n")
        f.write(f"OS={platform.system()} {platform.release()}\n")
        f.write(f"Football API Base URL={football_base}\n")
        f.write(f"GoRest API Base URL={gorest_base}\n")
        f.write(f"Test Environment={os.getenv('TEST_ENV', 'local')}\n")

    # Executor info - controls report name in Allure
    executor_file = results_dir / "executor.json"
    executor_info = {
        "name": os.getenv("EXECUTOR_NAME", "pytest"),
        "type": os.getenv("EXECUTOR_TYPE", "pytest"),
        "reportName": os.getenv("REPORT_NAME", "REST API Test Suite"),
        "buildName": os.getenv("BUILD_NAME", f"Build #{os.getenv('BUILD_NUMBER', '1')}"),
        "buildUrl": os.getenv("BUILD_URL", "")
    }

    with executor_file.open("w", encoding="utf-8") as f:
        json.dump(executor_info, f, indent=2)
