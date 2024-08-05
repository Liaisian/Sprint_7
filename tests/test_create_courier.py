import json
import requests
import allure
import url



class TestCreateCourier:

    @allure.title('Создание курьера')
    @allure.description('Проверка создания успешного запроса: статус 201; в ответе "{"ok": True}"')
    def test_create_courier_success(self, courier_data):
        payload = {
            "login": courier_data["login"],
            "password": courier_data["password"],
            "firstName": courier_data["firstName"]
        }

        response = requests.post(f'{url.SQOOTER_URL}/api/v1/courier', data=payload)
        assert response.status_code == 201 and response.json() == {"ok": True}

    @allure.description('Проверка создания двух одинаковых курьеров: статус 409; в ответе "Этот логин уже используется"')
    def test_create_duplicate_courier_fail(self, courier_data):
        payload = {
            "login": courier_data["login"],
            "password": courier_data["password"],
            "firstName": courier_data["firstName"]
        }

        response = requests.post(f'{url.SQOOTER_URL}/api/v1/courier', data=payload)
        assert response.status_code == 409 and response.text == "Этот логин уже используется"

    @allure.description('Проверка создания курьера без обязательных полей: статус 400; в ответе "Недостаточно данных для создания учетной записи"')
    def test_create_courier_without_required_fields_fail(self, courier_data):
        payload_missing_fields = [
            {"password": courier_data["password"], "firstName": courier_data["firstName"]},  # нет логина
            {"login": courier_data["login"], "firstName": courier_data["firstName"]},  # нет пароля
            {"login": courier_data["login"], "password": courier_data["password"]},  # нет имени
        ]

        for payload in payload_missing_fields:
            response = requests.post(f'{url.SQOOTER_URL}/api/v1/courier', data=payload)
            assert response.status_code == 400 and response.text == "Недостаточно данных для создания учетной записи"


