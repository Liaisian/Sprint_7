import requests
import url


class TestGetOrders:

    def test_active_completed_orders_for_courier(self):
        response = requests.get(f'{url.SQOOTER_URL}/api/v1/orders/?courierId=1')
        assert response.status_code == 200

    def test_orders_for_courier_at_stations(self):
        response = requests.get(f"{url.SQOOTER_URL}/api/v1/orders/?courierId=1&stationIds=[1,2]")
        assert response.status_code == 200

    def test_available_orders_for_courier(self):
        response = requests.get(f"{url.SQOOTER_URL}/api/v1/orders/?limit=10&page=0")
        assert response.status_code == 200

    def test_available_orders_near_station(self):
        response = requests.get(f"{url.SQOOTER_URL}/api/v1/orders/?limit=10&page=0&nearestStation=[110]")
        assert response.status_code == 200

    def test_successful_request_without_courier_id(self):
        response = requests.get(f'{url.SQOOTER_URL}/api/v1/orders/')
        assert response.status_code == 200

    def test_request_with_nonexistent_courier_id(self):
        nonexistent_courier_id = 9999  # Предполагаем, что 9999 не существует
        response = requests.get(f"{url.SQOOTER_URL}/api/v1/orders/?courierId={nonexistent_courier_id}")
        assert response.status_code == 404

