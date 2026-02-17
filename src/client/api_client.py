import requests

class ApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_users(self):
        return requests.get(f"{self.base_url}/users")

    def get_user(self, user_id: int):
        return requests.get(f"{self.base_url}/users/{user_id}")
    
    def create_user(self, user_data: dict):
        return requests.post(f"{self.base_url}/users", json=user_data)
    
    def update_user(self, user_id: int, user_data: dict):
        return requests.put(f"{self.base_url}/users/{user_id}", json=user_data)
    
    def delete_user(self, user_id: int):
        return requests.delete(f"{self.base_url}/users/{user_id}")