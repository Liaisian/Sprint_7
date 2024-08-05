import requests
import pytest
import allure
import url

class TestCreateOrder:

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        # Создание необходимых тестовых данных перед каждым тестом
        self.test_data = {
            "order_data": {
                "firstName": "Naruto",
                "lastName": "Uchiha",
                "address": "Konoha, 142 apt.",
                "metroStation": 4,
                "phone": "+7 800 355 35 35",
                "rentTime": 5,
                "deliveryDate": "2020-06-06",
                "comment": "Saske, come back to Konoha",
                "color": None
            }
        }
        yield
        # Удаление тестовых данных после каждого теста
        requests.delete(f'{url.SQOOTER_URL}/api/v1/orders/{self.test_data}')

    @pytest.mark.parametrize("color, expected_track", [
        ("BLACK", True),
        ("GREY", True),
        ("BLACK,GREY", True),
        (None, True),  # Тест без указания цвета
    ])
    @allure.title('Создание заказа')
    def test_create_order(self, color, expected_track):
        if color:
            self.test_data["order_data"]["color"] = color
        else:
            self.test_data["order_data"].pop("color", None)

        response = requests.post(f'{url.SQOOTER_URL}/api/v1/orders/', json=self.test_data["order_data"])

        assert response.status_code == 201  # Проверка успешного создания заказа
        response_data = response.json()

        if expected_track:
            assert "track" in response_data  # Проверка наличия поля track в ответе
        else:
            assert "track" not in response_data  # Проверка отсутствия поля track в ответе



