import requests
import allure


class ChangePost:
    url = 'http://167.172.172.115:52353/object'
    headers = {'Content-Type': 'application/json'}
    response = None

    @allure.step("Проверка существования объекта")
    def check_object_exists(self, object_id):
        response = requests.get(f'{self.url}/{object_id}')
        if response.status_code == 404:
            raise ValueError(f"Объект с ID {object_id} не найден.")
        return response.json()

    @allure.step("Обновление объекта")
    def new_post(self, object_id, body):
        self.response = requests.put(f'{self.url}/{object_id}', json=body, headers=self.headers)
        self.response.raise_for_status()
        self.json = self.response.json()

    @allure.step("Проверка ответа после обновления объекта")
    def assertions_message(self):
        assert self.response is not None, "Ответ сервера отсутствует."
        assert self.response.status_code == 200, "Ошибка: Не удалось обновить объект"
        assert 'id' in self.json, "Ошибка: В ответе отсутствует поле 'id'"
