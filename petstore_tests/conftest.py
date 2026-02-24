import pytest
import requests
from api_client import PetApiClient

BASE_URL = "https://petstore.swagger.io/v2"

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture()
def client(base_url):
    session = requests.Session()
    session.headers.update({"Content-Type": "application/json"})
    yield PetApiClient(session, base_url)
    session.close()