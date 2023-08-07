import requests


class UserService:
    base_url = "http://localhost:8080/api/user"

    def get_user(self, user_name):
        return requests.get(self.base_url + f"/{user_name}")
