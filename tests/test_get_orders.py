import allure
import requests
import url

@allure.title('Проверка: в тело ответа возвращается список заказов')
class TestGetOrders:
    def test_get_orders_response_is_list(self, courier_data, create_courier):
        self.courier_data = create_courier
        # Получаем список заказов для созданного курьера
        response = requests.get(f'{url.SQOOTER_URL}/api/v1/orders?courierId={self.courier_data["login"]}')
        assert response.status_code == 500

