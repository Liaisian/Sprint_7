import requests
import allure
import url

class TestLoginCourier:
    @allure.title('Логин курьера')
    @allure.description('Проверка успешного логина: статус 200; в ответе id')
    def test_login_courier_success_(self, create_courier):
        login_data = {
            "login": create_courier['login'],
            "password": create_courier['password']
        }

        response = requests.post(f'{url.SQOOTER_URL}/api/v1/courier/login', json=login_data)
        assert response.status_code == 200 and 'id' in response.json()

    @allure.description('Проверка: запрос без обязательных полей возвращает ошибку "Недостаточно данных для входа",статус 504')
    def test_login_missing_fields (self, create_courier):
        response = requests.post(f'{url.SQOOTER_URL}/api/v1/courier/login', json={})
        assert response.status_code == 504

    @allure.description('Проверка:неправильные логин или пароль возвращают ошибку "Учетная запись не найдена", статус 404')
    def test_login_invalid_credentials(self, create_courier):
        invalid_login_data = {
            "login": "wrong_username",
            "password": "wrong_password",
        }

        response = requests.post(f'{url.SQOOTER_URL}/api/v1/courier/login', json=invalid_login_data)
        assert response.status_code == 404

    @allure.description('Проверка:попытка авторизации под несуществующим пользователем возвращает ошибку')
    def test_login_nonexistent_user(self):
        nonexistent_login_data = {
            "login": "nonexistent_user",
            "password": "some_password",
        }

        response = requests.post(f'{url.SQOOTER_URL}/api/v1/courier/login', json=nonexistent_login_data)
        assert response.status_code == 404




