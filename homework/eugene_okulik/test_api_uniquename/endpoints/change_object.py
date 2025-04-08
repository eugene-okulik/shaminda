import requests
import allure
from test_api_uniquename.endpoints.base_endpoint import BaseEndpoint


class ChangeObject(BaseEndpoint):
    @allure.step("Обновление объекта")
    def update_object(self, object_id, body):
        self.response = requests.put(f'{self.url}/{object_id}', json=body, headers=self.headers)
        self.response.raise_for_status()
        self.json = self.response.json()

    @allure.step("Частичное обновление объекта")
    def patch_object(self, object_id, body):
        self.response = requests.patch(f'{self.url}/{object_id}', json=body, headers=self.headers)
        self.response.raise_for_status()
        self.json = self.response.json()
