from enum import Enum

from faker import Faker
from pydantic import EmailStr

from src.rest_api_client.go_rest_api.models import UserCreateRequest


fake = Faker()

class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"


class UserFactory:
    @staticmethod
    def create_active_user() -> UserCreateRequest:
        return UserCreateRequest(
            name=fake.name(),
            gender=fake.random_element(elements=(Gender.MALE.value, Gender.FEMALE.value)),
            email=fake.email(),
            status="active"
        )