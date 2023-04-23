from services.pet_service import PetService
import pytest
from faker import Faker

fake = Faker()


# pet_service = PetService()
@pytest.fixture()
def pet_service():
    return PetService()


@pytest.fixture()
def fake_pet(pet_service):
    json = {
        "category": {
            "id": 0,
            "name": "DoggieDog"
        },
        "name": fake.name(),
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "DoggieDog"
            }
        ],
        "status": "available"
    }
    response = pet_service.create_pet(json=json)
    return response.json()


def test_pet_find_by_id(pet_service):
    response = pet_service.get_pet(1)
    data = response.json()
    assert response.status_code == 200
    assert data["id"] == 1


def test_find_pets_by_status(pet_service):
    searched_status = "available"
    response = pet_service.get_pets_by_status(searched_status)
    data = response.json()
    assert response.status_code == 200
    for pet in data:
        assert pet["status"] == searched_status


def test_create_pet(pet_service, fake_pet):
    pet_id = fake_pet["id"]
    response = pet_service.create_pet(json=fake_pet)
    data = response.json()
    assert response.status_code == 200
    assert data["name"] == fake_pet["name"]
    assert data["id"] == pet_id


def test_update_fake_pet(pet_service, fake_pet):
    pet_id = fake_pet["id"]
    response = pet_service.create_pet(json=fake_pet)
    data = response.json()
    assert response.status_code == 200
    assert data["id"] == pet_id
    assert data["name"] == fake_pet["name"]
    updated_pet = fake_pet.copy()
    updated_pet["status"] = "unavailable"
    response = pet_service.update_pet(json=updated_pet)
    data = response.json()
    assert data["status"] == "unavailable"


def test_delete_pet(pet_service, fake_pet):
    pet_id = fake_pet["id"]
    response = pet_service.create_pet(json=fake_pet)
    data = response.json()
    assert response.status_code == 200
    assert data["id"] == pet_id
    assert data["name"] == fake_pet["name"]
    deleted_pet_response = pet_service.delete_pet(pet_id)
    assert deleted_pet_response.status_code == 200
    get_deleted_pet = pet_service.get_pet(pet_id)
    assert get_deleted_pet.status_code == 404
