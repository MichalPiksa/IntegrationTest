import dotenv
import pytest
from src.client.api_client import ApiClient
import os

@pytest.fixture(scope="session")
def api_client():
    dotenv.load_dotenv("data/.env")
    base_url = os.getenv("BASE_URL")
    if not base_url:
        raise ValueError("BASE_URL environment variable not set. Check data/.env or GitHub Actions secrets.")
    return ApiClient(base_url)