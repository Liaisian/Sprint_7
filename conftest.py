import requests
import url
from helpers import register_new_courier_and_return_login_password


#Создаем курьера
@classmethod
def setUpClass(cls):
    cls.courier_data = register_new_courier_and_return_login_password()
    payload = {
        "login": cls.courier_data["login"],
        "password": cls.courier_data["password"],
        "firstName": cls.courier_data["firstName"]
    }
    response = requests.post(f'{url.SQOOTER_URL}/api/v1/courier', data=payload)
    cls.courier_id = response.json().get('id')  # Сохраняем ID курьера для удаления позже

#Удаляем курьера
@classmethod
def tearDownClass(cls):
    if cls.courier_id:
        requests.delete(f'{url.SQOOTER_URL}/api/v1/courier/{cls.courier_id}')