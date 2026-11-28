import requests
import allure

from urls import Urls

class StellarBurgersApi:
    
    @staticmethod
    @allure.step("Создать пользователя")
    def register_user(payload):
        return requests.post(Urls.REGISTER, json=payload)

    @staticmethod
    @allure.step("Авторизоваться пользователем")
    def login_user(payload):
        return requests.post(Urls.LOGIN, json=payload)

    @staticmethod
    @allure.step("Удалить пользователя")
    def delete_user(token):
        return requests.delete(
            Urls.USER, 
            headers={"Authorization": token}
        )

    @staticmethod
    @allure.step("Получить список ингредиентов")
    def get_ingredients():
        return requests.get(Urls.INGREDIENTS)

    @staticmethod
    @allure.step("Создать заказ")
    def create_order(ingredients, token=None):
        headers = {}
        if token:
            headers["Authorization"] = token
        return requests.post(
            Urls.ORDERS, json={"ingredients": ingredients},
            headers=headers
        )
    