import requests
import pytest
import allure
import url

@allure.title('Создание заказа')
class TestCreateOrder:
    @pytest.mark.parametrize("colors, expected_status, expected_track", [
        (["BLACK"], 201, True),  # Один цвет
        (["GREY"], 201, True),  # Другой цвет
        (["BLACK", "GREY"], 201, True),  # Оба цвета
        ([], 201, True),  # Без указания цвета
    ])
    def test_create_order(self, colors, expected_status, expected_track):
        order_data = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": colors
        }

        response = requests.post(f'{url.SQOOTER_URL}/api/v1/orders', json=order_data)

        # Проверяем код ответа
        assert response.status_code == expected_status

        # Проверяем наличие поля track в ответе
        response_data = response.json()
        if expected_track:
            assert 'track' in response_data
        else:
            assert 'track' not in response_data




