import allure

from data import DataForUser, Messages
from api import StellarBurgersApi

@allure.feature("Логин пользователя")
class TestLoginUser:

    @allure.title("Вход под существующим пользователем")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_ok(self, user_with_token):
        payload = {
            "email": user_with_token["email"],
            "password": user_with_token["password"],
        }
        response = StellarBurgersApi.login_user(payload)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Вход с неверным логином")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_wrong_email(self, user_with_token):
        payload = {
            "email": DataForUser.INVALID_LOGIN_DATA_1["email"],
            "password": user_with_token["password"],
        }

        response = StellarBurgersApi.login_user(payload)

        assert response.status_code == 401
        assert response.json()["message"] == Messages.WRONG_CREDENTIALS
    
    @allure.title("Вход с неверным паролем")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_wrong_password(self, user_with_token):
        payload = {
            "email": user_with_token["email"],
            "password": DataForUser.INVALID_LOGIN_DATA_2["password"],
        }

        response = StellarBurgersApi.login_user(payload)

        assert response.status_code == 401
        assert response.json()["message"] == Messages.WRONG_CREDENTIALS
    
    @allure.title("Вход с неверным логином и паролем")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_wrong_credentials(self):
        payload = {
            "email": DataForUser.INVALID_LOGIN_DATA_3["email"],
            "password": DataForUser.INVALID_LOGIN_DATA_3["password"],
        }

        response = StellarBurgersApi.login_user(payload)

        assert response.status_code == 401
        assert response.json()["message"] == Messages.WRONG_CREDENTIALS
