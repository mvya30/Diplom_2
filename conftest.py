import pytest
import requests
import uuid

from urls import Urls

@pytest.fixture
def new_user():
    uid = uuid.uuid4().hex[:8]
    return {
        "email": f"test_{uid}@yandex.ru",
        "password": "password123",
        "name": f"User_{uid}",
    }

@pytest.fixture
def user_with_token(new_user):
    resp = requests.post(Urls.REGISTER, json=new_user)
    data = resp.json()
    yield {**new_user, "token": data["accessToken"]}
    requests.delete(Urls.USER, headers={"Authorization": data["accessToken"]})


@pytest.fixture
def ingredient_ids():
    resp = requests.get(Urls.INGREDIENTS)
    assert resp.status_code == 200
    return [i["_id"] for i in resp.json()["data"]]
