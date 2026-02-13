import pytest

from src.rest_api_client.exceptions import RestApiError
from src.rest_api_client.gorest_api.client import GoRestClient
from tests.factories.user_factory import UserFactory


@pytest.mark.negative
def test_invalid_gorest_token_returns_error(monkeypatch):
    monkeypatch.setenv("GOREST_TOKEN", "invalid_token")

    with GoRestClient() as gorest_client:
        with pytest.raises(RestApiError):
            gorest_client.get_user(1)

@pytest.mark.destructive
def test_deleting_user_twice_raises_error(gorest_client):
    create_payload = UserFactory.create_active_user()
    created = gorest_client.create_user(create_payload)
    user_id = created.id

    gorest_client.delete_user(user_id)

    with pytest.raises(RestApiError):
        gorest_client.delete_user(user_id)