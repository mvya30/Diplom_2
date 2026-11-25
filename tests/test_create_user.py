import allure
import requests
from data import Messages
from urls import Urls

@allure.feature("Создание пользователя")
class TestCreateUser:

    @allure.title("Успешное создание уникального пользователя")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_unique_user_success(self, new_user):
        resp = requests.post(Urls.REGISTER, json=new_user)
        assert resp.status_code == 200
        assert resp.json()["success"] is True
        requests.delete(Urls.USER, headers={"Authorization": resp.json()["accessToken"]})

    @allure.title("Создать уже зарегистрированного пользователя")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_duplicate_user(self, user_with_token):
        resp = requests.post(Urls.REGISTER, json={
            "email": user_with_token["email"],
            "password": user_with_token["password"],
            "name": user_with_token["name"],
        })
        assert resp.status_code == 403
        assert resp.json()["message"] == Messages.USER_ALREADY_EXISTS
    
    @allure.title("Создать пользователя без email")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_user_no_email(self, new_user):
        resp = requests.post(Urls.REGISTER, json={
            "password": new_user["password"],
            "name": new_user["name"],
        })
        assert resp.status_code == 403
        assert resp.json()["message"] == Messages.REQUIRED_FIELDS
        assert resp.json()["success"] is False

    @allure.title("Создать пользователя без password")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_user_no_password(self, new_user):
        resp = requests.post(Urls.REGISTER, json={
            "email": new_user["email"],
            "name": new_user["name"],
        })
        assert resp.status_code == 403
        assert resp.json()["message"] == Messages.REQUIRED_FIELDS
        assert resp.json()["success"] is False

    @allure.title("Создать пользователя без name")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_user_no_name(self, new_user):
        resp = requests.post(Urls.REGISTER, json={
            "email": new_user["email"],
            "password": new_user["password"],
        })
        assert resp.status_code == 403
        assert resp.json()["message"] == Messages.REQUIRED_FIELDS
        assert resp.json()["success"] is False
        