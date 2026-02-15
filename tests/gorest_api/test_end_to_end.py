import allure
import pytest

from rest_api_client.gorest_api.models import UserUpdateRequest
from tests.factories.user_factory import UserFactory


@pytest.mark.end2end
@pytest.mark.destructive
@allure.feature("User Management")
@allure.story("CRUD workflow")
@allure.severity(allure.severity_level.CRITICAL)
def test_user_crud_workflow(gorest_client):

    with allure.step("Create active user"):
        create_payload = UserFactory.create_active_user()
        created = gorest_client.create_user(create_payload)
        user_id = created.id

        assert created.email == create_payload.email, (
            f"Expected email {create_payload.email}, got {created.email}"
        )
        assert created.status == "active"

    try:
        with allure.step("Retrieve created user"):
            retrieved = gorest_client.get_user(user_id)
            assert retrieved.id == user_id, (
                f"Expected id {user_id}, got {retrieved.id}"
            )

        with allure.step("Update user name"):
            update_payload = UserUpdateRequest(name="Updated OlekUser")
            updated = gorest_client.update_user(user_id, update_payload)

            assert updated.name == "Updated OlekUser", (
                f"Expected updated name, got {updated.name}"
            )

    finally:
        with allure.step("Cleanup: delete created user"):
            gorest_client.delete_user(user_id)
