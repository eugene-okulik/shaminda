import requests
import allure
from test_api_uniquename.endpoints.base_endpoint import BaseEndpoint


class DeleteObject(BaseEndpoint):
    @allure.step("Удаление объекта")
    def delete_object(self, object_id):
        self.response = requests.delete(f'{self.url}/{object_id}', headers=self.headers)


        if self.response.status_code == 204:
            print(f"Объект с id {object_id} успешно удален.")
            self.json = None
        else:

            if 'application/json' in self.response.headers.get('Content-Type', ''):
                try:
                    self.json = self.response.json()
                except ValueError:
                    print(f"Ошибка: Не удалось декодировать ответ сервера. Ответ: {self.response.text}")
            else:
                print(f"Ответ сервера: {self.response.text}")
