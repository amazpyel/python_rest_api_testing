import pytest

from src.rest_api_client.exceptions import RestApiError
from src.rest_api_client.gorest_api.models import UserUpdateRequest
from tests.factories.user_factory import UserFactory

@pytest.mark.end2end
@pytest.mark.destructive
def test_user_crud_workflow(gorest_client):
    create_payload = UserFactory.create_active_user()
    created = gorest_client.create_user(create_payload)
    user_id = created.id

    try:
        # Retrieve user
        retrieved = gorest_client.get_user(user_id)
        assert retrieved.id == user_id

        # Update user
        update_payload = UserUpdateRequest(name="Updated OlekUser")
        updated = gorest_client.update_user(user_id, update_payload)
        assert updated.name == "Updated OlekUser"

    finally:
        gorest_client.delete_user(user_id)
