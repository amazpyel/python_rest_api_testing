from enum import StrEnum

from faker import Faker

from src.rest_api_client.gorest_api.models import UserCreateRequest

fake = Faker()


class Gender(StrEnum):
    MALE = "male"
    FEMALE = "female"


class UserFactory:
    @staticmethod
    def create_active_user() -> UserCreateRequest:
        return UserCreateRequest(
            name=fake.name(),
            gender=fake.random_element(elements=(Gender.MALE, Gender.FEMALE)),
            email=fake.email(),
            status="active",
        )
