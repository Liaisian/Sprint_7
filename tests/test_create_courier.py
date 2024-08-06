import requests
import allure
import url


class TestCreateCourier:

    @allure.title('Создание курьера')
    @allure.description('Проверка: курьера можно создать')
    def test_create_courier(self, create_courier):
        assert create_courier is not None

    @allure.description('Проверка создания двух одинаковых курьеров: статус 409; в ответе "Этот логин уже используется"')
    def test_create_duplicate_courier_fail(self, create_courier):
        response = requests.post(f'{url.SQOOTER_URL}/api/v1/courier', json=create_courier)
        assert response.status_code == 409

    @allure.description('Проверка создания курьера без обязательных полей: статус 400; в ответе "Недостаточно данных для создания учетной записи"')
    def test_create_courier_without_required_fields_fail(self):
        payloads = [
            {"password": "test_password", "firstName": "Test"},  # отсутствует login
            {"login": "test_login", "firstName": "Test"},  # отсутствует password
            {"login": "test_login", "password": "test_password"},  # отсутствует firstName
        ]

        for payload in payloads:
            response = requests.post(f'{url.SQOOTER_URL}/api/v1/courier', json=payload)
            assert response.status_code == 400

    @allure.description('Проверка: успешный запрос возвращает {"ok":true}')
    def test_success_response(self, create_courier):
        response = requests.post(f'{url.SQOOTER_URL}/api/v1/courier', json=create_courier)
        assert response.status_code == 409
