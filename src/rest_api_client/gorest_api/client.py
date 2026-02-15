import os

from rest_api_client.base_client import BaseRestApiClient
from rest_api_client.gorest_api.models import UserCreateRequest, UserResponse, UserUpdateRequest
from rest_api_client.http import HttpMethod


class GoRestClient(BaseRestApiClient):
    def __init__(self):
        token = os.getenv("GOREST_TOKEN")
        if not token:
            raise RuntimeError("GOREST_TOKEN is not set")

        super().__init__(
            base_url="https://gorest.co.in/public/v2",
            headers={"Authorization": f"Bearer {token}"},
        )

    def create_user(self, payload: UserCreateRequest) -> UserResponse:
        response = self._request(HttpMethod.POST, "/users", json=payload.model_dump())
        return UserResponse.model_validate(response.json())

    def get_user(self, user_id: int) -> UserResponse:
        response = self._request(HttpMethod.GET, f"/users/{user_id}")
        return UserResponse.model_validate(response.json())

    def update_user(self, user_id: int, payload: UserUpdateRequest) -> UserResponse:
        response = self._request(HttpMethod.PUT,f"/users/{user_id}", json=payload.model_dump(exclude_none=True))
        return UserResponse.model_validate(response.json())

    def delete_user(self, user_id: int):
        self._request(HttpMethod.DELETE, f"/users/{user_id}")
