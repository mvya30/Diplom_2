import pytest

from api import StellarBurgersApi
from helpers import generate_random_string


@pytest.fixture
def new_user():
    uid = generate_random_string()
    return {
        "email": f"test_{uid}@yandex.ru",
        "password": "password123",
        "name": f"User_{uid}",
    }

@pytest.fixture
def user_with_token(new_user):
    response = StellarBurgersApi.register_user(new_user)
    assert response.status_code == 200

    data = response.json()
    token = data["accessToken"]

    yield {
        **new_user, 
        "token": token,
        "registration_data": data,
    }

    StellarBurgersApi.delete_user(token)

@pytest.fixture
def ingredient_ids():
    response = StellarBurgersApi.get_ingredients()
    assert response.status_code == 200
    return [
        ingredient["_id"]
        for ingredient in response.json()["data"]
    ]
