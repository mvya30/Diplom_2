import allure

from api import StellarBurgersApi
from data import Messages
from urls import Urls

@allure.feature("Создание пользователя")
class TestCreateUser:

    @allure.title("Успешное создание уникального пользователя")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_unique_user_success(self, user_with_token):
        assert user_with_token["registration_data"]["success"] is True
        assert user_with_token["token"]

    @allure.title("Создать уже зарегистрированного пользователя")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_duplicate_user(self, user_with_token):
        payload = {
            "email": user_with_token["email"],
            "password": user_with_token["password"],
            "name": user_with_token["name"],
        }
        response = StellarBurgersApi.register_user(payload)

        assert response.status_code == 403
        assert response.json()["message"] == Messages.USER_ALREADY_EXISTS
    
    @allure.title("Создать пользователя без email")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_user_no_email(self, new_user):
        payload = {
            "password": new_user["password"],
            "name": new_user["name"],
        }
        response = StellarBurgersApi.register_user(payload)

        assert response.status_code == 403
        assert response.json()["message"] == Messages.REQUIRED_FIELDS
        assert response.json()["success"] is False

    @allure.title("Создать пользователя без password")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_user_no_password(self, new_user):
        payload = {
            "email": new_user["email"],
            "name": new_user["name"],
        }
        response = StellarBurgersApi.register_user(payload)

        assert response.status_code == 403
        assert response.json()["message"] == Messages.REQUIRED_FIELDS
        assert response.json()["success"] is False

    @allure.title("Создать пользователя без name")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_user_no_name(self, new_user):
        payload = {
            "email": new_user["email"],
            "password": new_user["password"],
        }
        response = StellarBurgersApi.register_user(payload)

        assert response.status_code == 403
        assert response.json()["message"] == Messages.REQUIRED_FIELDS
        assert response.json()["success"] is False
        