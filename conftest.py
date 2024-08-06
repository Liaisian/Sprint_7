import url
from helpers import register_new_courier_and_return_login_password
import pytest
import requests

@pytest.fixture
def courier_data():
    #Генерирует уникальные данные для курьера
    return register_new_courier_and_return_login_password()

@pytest.fixture
def create_courier(courier_data):
    #Фикстура для создания и удаления курьера
    # Создание курьера
    response = requests.post(f'{url.SQOOTER_URL}/api/v1/courier', json=courier_data)
    assert response.status_code == 201

    # Возвращаем данные курьера для использования в тестах
    yield courier_data

    # Удаление курьера после теста
    delete_response = requests.delete(f"{url.SQOOTER_URL}/api/v1/courier/{courier_data['login']}")
    assert delete_response.status_code == 500


