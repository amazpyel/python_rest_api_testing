import os
import random

from locust import HttpUser, between, task


class GoRestUser(HttpUser):
    wait_time = between(1, 2)

    def on_start(self):
        self.token = os.getenv("GOREST_TOKEN")
        if not self.token:
            raise RuntimeError("GOREST_TOKEN is not set")

    def _headers(self):
        return {"Authorization": f"Bearer {self.token}"}

    @task(3)
    def get_users_list(self):
        with self.client.get(
            "/users",
            headers=self._headers(),
            name="GET /users",
            catch_response=True,
        ) as response:
            if response.status_code != 200:
                response.failure(f"Unexpected status: {response.status_code}")
            elif response.elapsed.total_seconds() > 0.5:
                response.failure("SLA exceeded (500ms)")

    @task(1)
    def get_single_user(self):
        user_id = random.randint(1, 5000)
        with self.client.get(
            f"/users/{user_id}",
            headers=self._headers(),
            name="GET /users/{id}",
            catch_response=True,
        ) as response:
            if response.status_code not in (200, 404):
                response.failure(f"Unexpected status: {response.status_code}")
            elif response.elapsed.total_seconds() > 0.5:
                response.failure("SLA exceeded (500ms)")