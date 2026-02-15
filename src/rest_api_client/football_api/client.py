import os
from rest_api_client.base_client import BaseRestApiClient
from rest_api_client.football_api.models import AreasResponse
from rest_api_client.http import HttpMethod


class FootballApiClient(BaseRestApiClient):
    def __init__(self):
        token = os.getenv("FOOTBALL_DATA_TOKEN")
        if not token:
            raise RuntimeError("FOOTBALL_DATA_TOKEN is not set")

        super().__init__(
            base_url="https://api.football-data.org/v4",
            headers={"X-Auth-Token": token},
        )

    def get_areas(self):
        response = self._request(HttpMethod.GET, "/areas")
        return AreasResponse.model_validate(response.json())