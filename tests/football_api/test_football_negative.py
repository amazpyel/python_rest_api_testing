import allure
import pytest

from rest_api_client.exceptions import RestApiError
from rest_api_client.football_api.client import FootballApiClient


@allure.feature("Authorization")
@allure.story("Invalid API token")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.negative
def test_invalid_football_api_token_returns_error(monkeypatch):

    with allure.step("Override FOOTBALL_DATA_TOKEN with invalid value"):
        monkeypatch.setenv("FOOTBALL_DATA_TOKEN", "invalid_token")

    with (
        allure.step("Call GET /areas and expect authorization failure"),
        FootballApiClient() as football_client,
        pytest.raises(RestApiError) as exc_info,
    ):
        football_client.get_areas()

    with allure.step("Validate error message indicates auth failure"):
        error_message = str(exc_info.value)

        assert "401" in error_message or "403" in error_message, (
            f"Unexpected error message: {error_message}"
        )
