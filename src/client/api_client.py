import requests

class ApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_users(self):
        return requests.get(f"{self.base_url}/users")

    def get_user(self, user_id: int):
        return requests.get(f"{self.base_url}/users/{user_id}")