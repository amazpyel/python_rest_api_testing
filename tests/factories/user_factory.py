from enum import StrEnum

from faker import Faker

from rest_api_client.gorest_api.models import UserCreateRequest

fake = Faker()


class Gender(StrEnum):
    MALE = "male"
    FEMALE = "female"


class UserFactory:
    @staticmethod
    def build(
        name: str | None = None,
        gender: str | None = None,
        email: str | None = None,
        status: str = "active",
    ) -> UserCreateRequest:
        return UserCreateRequest(
            name=name or fake.name(),
            gender=gender or fake.random_element(elements=(Gender.MALE, Gender.FEMALE)),
            email=email or fake.email(),
            status=status,
        )

    @staticmethod
    def create_active_user() -> UserCreateRequest:
        return UserFactory.build(status="active")