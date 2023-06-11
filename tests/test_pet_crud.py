import pytest
from hamcrest import *
from services.payload_generator import create_pet_payload


def test_pet_find_by_id(pet_service):
    (response, pet) = pet_service.get_pet(1)
    # data = response.json()
    assert_that(response.status_code, equal_to(200))
    # assert_that(pet.id, equal_to(1))
    assert pet.id == 1


def test_find_pets_by_status(pet_service):
    searched_status = "available"
    response = pet_service.get_pets_by_status(searched_status)
    data = response.json()
    assert_that(response.status_code, equal_to(200))
    for pet in data:
        assert_that(pet["status"], is_(searched_status))


def test_create_pet(pet_service, fake_pet):
    pet_id = fake_pet["id"]
    response = pet_service.create_pet(params=fake_pet)
    data = response.json()
    assert_that(response.status_code, is_(200))
    assert_that(data["name"], is_(fake_pet["name"]))
    assert_that(data["id"], is_(pet_id))


def test_update_fake_pet(pet_service, fake_pet):
    pet_id = fake_pet["id"]
    response = pet_service.create_pet(params=fake_pet)
    data = response.json()
    assert_that(response.status_code, is_(200))
    assert_that(data["id"], is_(pet_id))
    assert_that(data["name"], is_(fake_pet["name"]))
    updated_pet = fake_pet.copy()
    updated_pet["status"] = "unavailable"
    response = pet_service.update_pet(params=updated_pet)
    data = response.json()
    assert_that(response.status_code, is_(200))
    assert_that(data["status"], is_("unavailable"))


def test_delete_pet(pet_service, fake_pet):
    pet_id = fake_pet["id"]
    response = pet_service.create_pet(params=fake_pet)
    data = response.json()
    assert_that(response.status_code, is_(200))
    assert_that(data["id"], is_(pet_id))
    assert_that(data["name"], is_(fake_pet["name"]))
    deleted_pet_response = pet_service.delete_pet(pet_id)
    assert_that(deleted_pet_response.status_code, is_(200))
    get_deleted_pet = pet_service.get_pet(pet_id)
    assert_that(get_deleted_pet.status_code, is_(404))


@pytest.mark.parametrize("name", [("user1"), ("user2"), ("user3"), ("user4")])
def test_get_users(user_service, name):
    response = user_service.get_user(user_name=name)
    assert_that(response.status_code, is_(404))


@pytest.mark.parametrize("id", ["1", "2", "3", "4"])
def test_get_pets_by_ids(pet_service, id):
    response = pet_service.get_pet(pet_id=id)
    assert_that(response.status_code, is_(200))


@pytest.mark.parametrize("xyz", [{"name": "pet1", "status": "unavailable"}, {"name": "pet2"}])
def test_create_pet_param(pet_service, xyz):
    payload = create_pet_payload(**xyz)

    print(payload)
