import os

import allure
import pytest

from tests.factories.user_factory import UserFactory

USER_FIELD_COMBINATIONS = [
    pytest.param("male", "active", id="male-active"),
    pytest.param("female", "active", id="female-active"),
    pytest.param("male", "inactive", id="male-inactive"),
    pytest.param("female", "inactive", id="female-inactive"),
]


@pytest.mark.destructive
@pytest.mark.parametrize(("gender", "status"), USER_FIELD_COMBINATIONS)
@pytest.mark.skipif(
    os.getenv("CI") == "true", reason="GoRest blocks CI/CD environments (CloudFlare protection)"
)
@allure.feature("User Management")
@allure.story("Create user with field variations")
@allure.severity(allure.severity_level.NORMAL)
def test_create_user_field_combinations(gorest_client, gender, status):

    with allure.step(f"Create user with gender={gender!r}, status={status!r}"):
        payload = UserFactory.build(gender=gender, status=status)
        created = gorest_client.create_user(payload)

    try:
        with allure.step("Validate persisted field values match the request"):
            assert created.gender == gender, f"Expected gender {gender!r}, got {created.gender!r}"
            assert created.status == status, f"Expected status {status!r}, got {created.status!r}"
            assert created.email == payload.email, (
                f"Expected email {payload.email!r}, got {created.email!r}"
            )

    finally:
        with allure.step("Cleanup: delete created user"):
            gorest_client.delete_user(created.id)
