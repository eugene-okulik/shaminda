import requests
import allure
from test_api_uniquename.endpoints.base_endpoint import BaseEndpoint


class CreateObject(BaseEndpoint):
    @allure.step("Создание нового объекта")
    def create_object(self, body):
        self.response = requests.post(self.url, json=body, headers=self.headers)
        self.response.raise_for_status()
        self.json = self.response.json()
