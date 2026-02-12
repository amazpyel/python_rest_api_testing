import os
import httpx


class RestApiClient:
    BASE_URL = "https://api.football-data.org/v4"

    def __init__(self):
        token = os.getenv("FOOTBALL_DATA_TOKEN")
        if not token:
            raise RuntimeError("FOOTBALL_DATA_TOKEN is not set")

        self._client = httpx.Client(
            base_url=self.BASE_URL,
            headers={"X-Auth-Token": token},
            timeout=10.0,
        )

    def get_areas(self):
        response = self._client.get("/areas")
        response.raise_for_status()
        return response.json()

    def close(self):
        self._client.close()
