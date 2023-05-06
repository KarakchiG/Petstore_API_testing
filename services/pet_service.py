import requests


class PetService:
    url = "http://localhost:8080/api/pet"

    def get_pet(self, pet_id):
        return requests.get(self.url + f"/{pet_id}")

    def get_pets_by_status(self, status):
        return requests.get(f"{self.url}/findByStatus?status={status}")

    def create_pet(self, params):
        return requests.post(self.url, json=params)

    def update_pet(self, params):
        return requests.put(self.url, json=params)

    def delete_pet(self, pet_id):
        return requests.delete(self.url + f"/{pet_id}")
