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
            name=name if name is not None else fake.name(),
            gender=gender if gender is not None else fake.random_element(elements=(Gender.MALE, Gender.FEMALE)),
            email=email if email is not None else fake.email(),
            status=status,
        )

    @staticmethod
    def create_active_user() -> UserCreateRequest:
        return UserFactory.build(status="active")