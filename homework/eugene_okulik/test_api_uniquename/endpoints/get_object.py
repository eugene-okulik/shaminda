import requests
import allure
from test_api_uniquename.endpoints.base_endpoint import BaseEndpoint


class GetObject(BaseEndpoint):
    @allure.step("Получение объекта по ID")
    def get_object(self, object_id):
        self.response = requests.get(f'{self.url}/{object_id}', headers=self.headers)
        self.response.raise_for_status()
        return self.response.json()
