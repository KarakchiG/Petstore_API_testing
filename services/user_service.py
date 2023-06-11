import requests


class UserService:
    base_url = "http://localhost:8080/api/store/user"

    def get_user(self, user_name):
        return requests.get(self.base_url + f"/{user_name}")

# u = UserService()
# print(u.get_user(user_name="user1"))
#
# res = requests.get("http://localhost:8080/api/store/user/user1")
# print(res.status_code)
