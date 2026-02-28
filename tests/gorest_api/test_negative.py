import contextlib
import os

import allure
import pytest

from rest_api_client.exceptions import AuthError, NotFoundError, RestApiError
from rest_api_client.gorest_api.client import GoRestClient
from tests.factories.user_factory import UserFactory


@allure.feature("Authorization")
@allure.story("Invalid GoRest token")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.negative
def test_invalid_gorest_token_returns_error(monkeypatch):

    with allure.step("Override GOREST_TOKEN with invalid value"):
        monkeypatch.setenv("GOREST_TOKEN", "invalid_token")

    with (
        allure.step("Call GET /users/{id} and expect authorization failure"),
        GoRestClient() as gorest_client,
        pytest.raises(AuthError),
    ):
        gorest_client.get_user(1)


@allure.feature("User Management")
@allure.story("Delete user twice")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.negative
@pytest.mark.destructive
@pytest.mark.skipif(
    os.getenv("CI") == "true", reason="GoRest blocks CI/CD environments (CloudFlare protection)"
)
def test_deleting_user_twice_raises_error(gorest_client):

    with allure.step("Create user"):
        create_payload = UserFactory.create_active_user()
        created = gorest_client.create_user(create_payload)
        user_id = created.id

    try:
        with allure.step("Delete user first time"):
            gorest_client.delete_user(user_id)

        with allure.step("Delete user second time and expect failure"), pytest.raises(NotFoundError):
            gorest_client.delete_user(user_id)

    finally:
        # Ensure no leftovers in case logic changes
        with contextlib.suppress(RestApiError):
            gorest_client.delete_user(user_id)
