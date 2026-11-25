import allure
import requests
from urls import Urls
from data import Messages

@allure.feature("Создание заказа")
class TestCreateOrder:
    @allure.title("Создать заказ с авторизацией и ингредиентами")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_order_with_auth(self, user_with_token, ingredient_ids):
        resp = requests.post(
            Urls.ORDERS,
            json={"ingredients": ingredient_ids[:2]},
            headers={"Authorization": user_with_token["token"]},
        )
        assert resp.status_code == 200
        assert resp.json()["success"] is True

    @allure.title("Создать заказ без авторизации")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_order_without_auth(self, ingredient_ids):
        resp = requests.post(Urls.ORDERS, json={"ingredients": ingredient_ids[:2]})
        assert resp.status_code == 200

    @allure.title("Создать заказ с ингредиентами")
    @allure.severity(allure.severity_level.NORMAL)
    def test_order_with_ingredients(self, user_with_token, ingredient_ids):
        resp = requests.post(
            Urls.ORDERS,
            json={"ingredients": ingredient_ids[:2]},
            headers={"Authorization": user_with_token["token"]},
        )
        assert resp.status_code == 200
        data = resp.json()
        assert data["success"] is True
        assert "order" in data
        assert "number" in data["order"]
        allure.attach(str(data["order"]["number"]), name="Номер заказа",
                    attachment_type=allure.attachment_type.TEXT)

    @allure.title("Создать заказ без ингредиентов")
    @allure.severity(allure.severity_level.NORMAL)
    def test_order_without_ingredients(self, user_with_token):
        resp = requests.post(
            Urls.ORDERS,
            json={"ingredients": []},
            headers={"Authorization": user_with_token["token"]},
        )
        assert resp.status_code == 400
        assert resp.json()["message"] == Messages.INGREDIENTS_REQUIRED

    @allure.title("Создать заказ с неверным хешем ингредиента")
    @allure.severity(allure.severity_level.NORMAL)
    def test_order_bad_hash(self, user_with_token):
        resp = requests.post(
            Urls.ORDERS,
            json={"ingredients": ["bad_hash"]},
            headers={"Authorization": user_with_token["token"]},
        )
        assert resp.status_code == 500
