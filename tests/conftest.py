from services.pet_service import PetService
from services.user_service import UserService
import pytest
from faker import Faker

fake = Faker()


@pytest.fixture()
def pet_service():
    return PetService()


@pytest.fixture()
def user_service():
    return UserService()


class PetCreationError(Exception):
    pass


@pytest.fixture()
def created_pet(pet_service, **kwargs):
    params = {
        "category": {
            "id": kwargs.get("id", 1),
            "name": kwargs.get("category_name", "Dog")
        },
        "name": kwargs.get("name", fake.name()),
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "Dog"
            }
        ],
        "status": "available"
    }
    response = pet_service.create_pet(params)
    if response.status_code != 200:
        raise PetCreationError(f"Pet creation failed with error: {response.content}")
    else:
        return response.json()
