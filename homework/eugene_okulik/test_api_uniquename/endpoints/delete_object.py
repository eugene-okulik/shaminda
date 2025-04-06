import requests
import allure
from test_api_uniquename.endpoints.base_endpoint import BaseEndpoint


class DeleteObject(BaseEndpoint):
    @allure.step("Удаление объекта")
    def delete_object(self, object_id):
        body = {"id": object_id}
        self.response = requests.delete(self.url, json=body, headers=self.headers)
        self.response.raise_for_status()
