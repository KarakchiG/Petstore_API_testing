import requests
from dataclasses import dataclass


@dataclass()
class Pet:
    id: int
    name: str
    status: str
    category: {"id": int, "name": str}
    tags: [{"id": int, "name": str}]
    photoUrls: [str]

    def __repr__(self):
        return f"Pet(name={self.name})"


class PetService:
    url = "http://localhost:8080/api/pet"

    def get_pet(self, pet_id):
        response = requests.get(self.url + f"/{pet_id}")
        return response, Pet(**response.json())

    def get_pets_by_status(self, status):
        return requests.get(f"{self.url}/findByStatus?status={status}")

    def create_pet(self, params):
        return requests.post(self.url, json=params)

    def update_pet(self, params):
        return requests.put(self.url, json=params)

    def delete_pet(self, pet_id):
        return requests.delete(self.url + f"/{pet_id}")
