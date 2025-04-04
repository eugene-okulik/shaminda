import requests
import allure
from test_api_uniquename.endpoints.base_post import BasePost


class DeleteObject(BasePost):
    @allure.step("Удаление объекта")
    def delete_object(self, object_id):
        body = {"id": object_id}
        self.response = requests.delete(self.url, json=body, headers=self.headers)
        self.response.raise_for_status()

    @allure.step("Проверка, что объект удалён")
    def check_object_deleted(self, object_id):
        response = requests.get(f"{self.url}/{object_id}", headers=self.headers)
        return response.status_code == 404
