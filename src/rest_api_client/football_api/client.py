import os

from rest_api_client.base_client import BaseRestApiClient
from rest_api_client.football_api.models import AreasResponse, Competition, CompetitionsResponse
from rest_api_client.http import HttpMethod

_DEFAULT_BASE_URL = "https://api.football-data.org/v4"


class FootballApiClient(BaseRestApiClient):
    def __init__(self):
        token = os.getenv("FOOTBALL_DATA_TOKEN")
        if not token:
            raise RuntimeError("FOOTBALL_DATA_TOKEN is not set")

        super().__init__(
            base_url=os.getenv("FOOTBALL_BASE_URL", _DEFAULT_BASE_URL),
            headers={"X-Auth-Token": token},
        )

    def get_areas(self) -> AreasResponse:
        response = self._request(HttpMethod.GET, "/areas")
        return AreasResponse.model_validate(response.json())

    def get_competitions(self) -> CompetitionsResponse:
        response = self._request(HttpMethod.GET, "/competitions")
        return CompetitionsResponse.model_validate(response.json())

    def get_competition(self, competition_id: int) -> Competition:
        response = self._request(HttpMethod.GET, f"/competitions/{competition_id}")
        return Competition.model_validate(response.json())