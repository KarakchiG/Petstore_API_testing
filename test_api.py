import requests


def test_find_pets_by_status():
    response = requests.get("http://localhost:8080/api/pet/findByStatus?status=available")
    assert response.status_code == 200


url = "http://localhost:8080/api/pet"


def test_create_pet_response():
    params = create_pet_params()
    create_pet_response = create_pet(params)
    assert create_pet_response.status_code == 200

    data = create_pet_response.json()

    pet_id = data['id']
    get_pet_response = get_pet(pet_id)
    assert get_pet_response.status_code == 200
    get_pet_data = get_pet_response.json()
    assert get_pet_data is not None
    assert get_pet_data['name'] == params['name']
    assert get_pet_data['status'] == params['status']


def test_update_pet():
    # create pet
    params = create_pet_params()
    create_pet_response = create_pet(params)
    assert create_pet_response.status_code == 200
    pet_id = create_pet_response.json()['id']

    # update pet
    new_params = {
        "id": pet_id,
        "category": {
            "id": 0,
            "name": "Bunny"
        },
        "name": "DoggieDog",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "DoggieDog"
            }
        ],
        "status": "unavailable"
    }
    update_pet_response = update_pet(new_params)
    assert update_pet_response.status_code == 200

    # get and validate changes
    get_pet_response = get_pet(pet_id)
    assert get_pet_response.status_code == 200
    get_pet_data = get_pet_response.json()
    assert get_pet_data["category"] == new_params["category"]
    assert get_pet_data["status"] == new_params["status"]


def test_delete_pet():
    # Create
    params = create_pet_params()
    create_pet_response = create_pet(params)
    assert create_pet_response.status_code == 200
    pet_id = create_pet_response.json()['id']

    # Delete
    delete_pet_response = delete_pet(pet_id)
    assert delete_pet_response.status_code == 200

    # get the deleted pet
    get_pet_response = get_pet(pet_id)
    assert get_pet_response.status_code == 404


# helper functions
def create_pet(params):
    return requests.post(url, json=params)


def update_pet(params):
    return requests.put(url, json=params)


def get_pet(pet_id):
    return requests.get(url + "/" + str(pet_id))


def create_pet_params():
    return {
        "id": 0,
        "category": {
            "id": 0,
            "name": "DoggieDog"
        },
        "name": "DoggieDog",
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


def delete_pet(pet_id):
    return requests.delete(url + "/" + str(pet_id))
