import pytest
from src.client.api_client import ApiClient
import os

@pytest.fixture(scope="session")
def api_client():
    base_url = os.getenv("BASE_URL", "https://jsonplaceholder.typicode.com")
    return ApiClient(base_url)