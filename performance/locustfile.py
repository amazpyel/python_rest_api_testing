from locust import HttpUser, task, between
import os


class GoRestUser(HttpUser):
    wait_time = between(1, 2)

    def on_start(self):
        self.token = os.getenv("GOREST_TOKEN")
        if not self.token:
            raise RuntimeError("GOREST_TOKEN is not set")

    @task
    def get_user(self):
        headers = {
            "Authorization": f"Bearer {self.token}"
        }

        with self.client.get(
            "/users/1",
            headers=headers,
            name="GET /users/{id}",
            catch_response=True,
        ) as response:

            if response.status_code != 200:
                response.failure(
                    f"Unexpected status: {response.status_code}"
                )

            elif response.elapsed.total_seconds() > 0.5:
                response.failure("SLA exceeded (500ms)")
