import allure

from data import Messages
from api import StellarBurgersApi

@allure.feature("Создание заказа")
class TestCreateOrder:
    @allure.title("Создать заказ с авторизацией и ингредиентами")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_order_with_auth(self, user_with_token, ingredient_ids):
        response = StellarBurgersApi.create_order(
            ingredient_ids[:2],
            user_with_token["token"]
        )
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создать заказ без авторизации")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_order_without_auth(self, ingredient_ids):
        response = StellarBurgersApi.create_order(ingredient_ids[:2])
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создать заказ с ингредиентами")
    @allure.severity(allure.severity_level.NORMAL)
    def test_order_with_ingredients(self, user_with_token, ingredient_ids):
        response = StellarBurgersApi.create_order(
            ingredient_ids[:2],
            user_with_token["token"]
        )
        data = response.json()
        
        assert response.status_code == 200
        assert data["success"] is True
        assert "order" in data
        assert "number" in data["order"]
        
    @allure.title("Создать заказ без ингредиентов")
    @allure.severity(allure.severity_level.NORMAL)
    def test_order_without_ingredients(self, user_with_token):
        response = StellarBurgersApi.create_order(
            [],
            user_with_token["token"]
        )
        assert response.status_code == 400
        assert response.json()["message"] == Messages.INGREDIENTS_REQUIRED

    @allure.title("Создать заказ с неверным хешем ингредиента")
    @allure.severity(allure.severity_level.NORMAL)
    def test_order_bad_hash(self, user_with_token):
        response = StellarBurgersApi.create_order(
            ["bad_hash"],
            user_with_token["token"]
        )
        assert response.status_code == 500
