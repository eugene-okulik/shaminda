import requests
import allure
from test_api_uniquename.endpoints.base_endpoint import BaseEndpoint


class GetPost(BaseEndpoint):
    @allure.step("Получение объекта по ID")
    def get_object(self, object_id):
        self.response = requests.get(f'{self.url}/{object_id}', headers=self.headers)
        self.response.raise_for_status()
        return self.response.json()

    @allure.step("Проверка существования объекта")
    def check_object_exists(self, object_id):
        response = self.get_object(object_id)
        assert response is not None, f"Объект с ID {object_id} не найден."
        return response
