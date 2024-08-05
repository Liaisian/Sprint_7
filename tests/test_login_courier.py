import requests
import allure
import url



class TestLoginCourier:

    @allure.title('Логин курьера')
    @allure.description('Проверка успешного логина: статус 200; в ответе id')
    def test_login_courier_success_(self, courier_data):
        response = requests.post(f'{url.SQOOTER_URL}/api/v1/courier/login', json= courier_data)
        assert response.status_code == 200 and response.json() == {id: 12345}

    @allure.description('Проверка: запрос без обязательных полей возвращает ошибку "Недостаточно данных для входа",статус 400')
    def test_login_requires_all_fields(self, courier_data):
        response = requests.post(f'{url.SQOOTER_URL}/api/v1/courier/login', json={"login": courier_data["login"]})
        assert response.status_code == 400 and response.text == "Недостаточно данных для входа"

    @allure.description('Проверка:неправильные логин или пароль возвращают ошибку "Учетная запись не найдена", статус 404')
    def test_incorrect_login_or_password(self):
        response = requests.post(f'{url.SQOOTER_URL}/api/v1/courier/login',
                                 json={"login": "wrong_login", "password": "wrong_password"})
        assert response.status_code == 404 and response.text == "Учетная запись не найдена"

    @allure.description('Проверка:попытка авторизации под несуществующим пользователем возвращает ошибку')
    def test_nonexistent_user(self):
        response = requests.post(f'{url.SQOOTER_URL}/api/v1/courier/login',
                                 json={"login": "nonexistent_user", "password": "some_password"})
        assert response.status_code == 404 and response.text == "Учетная запись не найдена"

    @allure.description('Проверка: запрос без обязательных полей возвращает ошибку "Недостаточно данных для входа",статус 400')
    def test_missing_field_returns_error(self, courier_data):
        response = requests.post(f'{url.SQOOTER_URL}/api/v1/courier/login', json={"password": courier_data["password"]})
        assert response.status_code == 400 and response.text == "Недостаточно данных для входа"



