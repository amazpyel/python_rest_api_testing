import pytest

from src.rest_api_client.exceptions import RestApiError
from tests.factories.user_factory import UserFactory


def test_user_crud_workflow(gorest_client):
    create_payload = UserFactory.create_active_user()

    created = gorest_client.create_user(create_payload)
    user_id = created.id

    assert created.email == create_payload.email

    gorest_client.delete_user(user_id)

    with pytest.raises(RestApiError):
        gorest_client.get_user(user_id)