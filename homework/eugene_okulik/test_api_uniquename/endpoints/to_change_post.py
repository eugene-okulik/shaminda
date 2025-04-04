import requests
import allure
from test_api_uniquename.endpoints.base_post import BasePost


class ChangePost(BasePost):
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

    @allure.step("Проверка существования объекта")
    def check_object_exists(self, object_id):
        response = requests.get(f'{self.url}/{object_id}', headers=self.headers)
        assert response.status_code != 404, f"Объект с ID {object_id} не найден."
        return response.json()
