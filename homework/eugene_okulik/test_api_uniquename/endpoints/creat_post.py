

import requests
import allure

class CreatPost:
    url = 'http://167.172.172.115:52353/object'
    headers = {'Content-Type': 'application/json'}
    response = None
    json = None
    body = None  # Добавлено для хранения тела запроса

    @allure.step("Создание нового объекта")
    def new_post(self, body):
        self.body = body  # Сохраняем тело запроса
        self.response = requests.post(self.url, json=body, headers=self.headers)
        self.response.raise_for_status()  # Проверка на ошибки HTTP
        self.json = self.response.json()
        return self.response

    @allure.step("Проверка ответа после создания объекта")
    def assertions_message(self):
        assert self.response is not None, "Ответ сервера отсутствует."
        assert self.response.status_code == 200, "Ошибка: Не удалось создать объект"
        assert self.json is not None, "Ошибка: Ответ не является валидным JSON."
        assert 'id' in self.json, "Ошибка: В ответе отсутствует поле 'id'"
        assert self.json['name'] == self.body['name'], "Ошибка: Имя объекта не совпадает"

    def get_object_id(self):
        return self.json.get('id')
