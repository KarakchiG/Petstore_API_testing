import pytest
from hamcrest import *


def test_pet_find_by_id(pet_service):
    response, pet = pet_service.get_pet(1)
    assert_that(response.status_code, equal_to(200), f"Response failed with content: {response.content}")
    assert_that(pet.id, equal_to(1))


def test_find_pets_by_status(pet_service):
    searched_status = "available"
    response = pet_service.get_pets_by_status(searched_status)

    assert_that(response.status_code, equal_to(200), f"Response failed with content: {response.content}")

    data = response.json()
    for pet in data:
        assert_that(pet["status"], equal_to(searched_status))


def test_create_pet(pet_service, created_pet):
    pet_id = created_pet["id"]
    response = pet_service.create_pet(params=created_pet)

    assert_that(response.status_code, equal_to(200), f"Response failed with content: {response.content}")

    data = response.json()
    assert_that(data["name"], equal_to(created_pet["name"]))
    assert_that(data["id"], equal_to(pet_id))


def test_update_fake_pet(pet_service, created_pet):
    assert_that(created_pet["status"], equal_to("available"))

    created_pet["status"] = "unavailable"

    response = pet_service.update_pet(params=created_pet)
    assert_that(response.status_code, equal_to(200), f"Response failed with content: {response.content}")

    data = response.json()
    assert_that(data["status"], equal_to("unavailable"))


def test_delete_pet(pet_service, created_pet):
    pet_id = created_pet["id"]
    response = pet_service.create_pet(params=created_pet)
    assert_that(response.status_code, equal_to(200), f"Response failed with content: {response.content}")

    data = response.json()
    assert_that(data["id"], equal_to(pet_id))
    assert_that(data["name"], equal_to(created_pet["name"]))

    deleted_pet_response = pet_service.delete_pet(pet_id)
    assert_that(deleted_pet_response.status_code, equal_to(200), f"Response failed with content: {response.content}")

    get_deleted_pet = pet_service.get_pet(pet_id)
    assert_that(get_deleted_pet.status_code, equal_to(404), f"Response failed with content: {response.content}")


@pytest.mark.parametrize("name", [("2user"), ("3user"), ("4user")])
def test_get_users(user_service, name):
    response = user_service.get_user(user_name=name)
    assert_that(response.status_code, equal_to(404), f"Response failed with content: {response.content}")

    data = response.json()
    assert_that(data["message"], equal_to("User not found"))

    assert_that(data.values(), is_not(has_item("2user")))
    assert_that(data.values(), is_not(has_item("3user")))
    assert_that(data.values(), is_not(has_item("4user")))


@pytest.mark.parametrize("name", [("user1"), ("user2"), ("user3"), ("user4")])
def test_get_user_by_name(user_service, name):
    response = user_service.get_user(user_name=name)
    assert_that(response.status_code, equal_to(200), f"Response failed with content: {response.content}")

    data = response.json()
    assert_that(data, is_not(empty()))

    assert_that(data, has_key("id"))
    assert_that(data, has_key("username"))
    assert_that(data, has_key("password"))
    assert_that(data, has_key("email"))
    assert_that(data, has_key("phone"))
    assert_that(data, has_key("userStatus"))

    assert_that(data["username"], equal_to(name))


@pytest.mark.parametrize("id", [1, 2, 3, 4])
def test_get_pets_by_ids(pet_service, id):
    response, pet = pet_service.get_pet(pet_id=id)
    assert_that(response.status_code, equal_to(200), f"Response failed with content: {response.content}")

    data = response.json()
    assert_that(data, is_not(empty()))
    for pet_data in data:
        assert_that(pet.id, equal_to(id))
