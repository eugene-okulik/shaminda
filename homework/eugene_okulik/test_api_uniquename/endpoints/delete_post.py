import requests
from test_api_uniquename.endpoints.creat_post import CreatPost


import allure


class DeleteObject(CreatPost):
    @allure.step("Удаление объекта")
    def delete_obj(self, object_id):
        body = {"id": object_id}
        self.response = requests.delete(self.url, json=body, headers=self.headers)
        self.response.raise_for_status()

    @allure.step("Проверка ответа после удаления объекта")
    def assertions_message(self):
        assert self.response is not None, "Ответ сервера отсутствует."
        assert self.response.status_code == 200, "Ошибка: Не удалось удалить объект"

    @allure.step("Проверка, что объект удалён")
    def check_object_deleted(self, object_id):
        response = requests.get(f"{self.url}/{object_id}", headers=self.headers)
        return response.status_code == 404  # Вернуть True, если объект удалён

