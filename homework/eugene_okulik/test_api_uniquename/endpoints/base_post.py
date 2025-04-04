
class BasePost:
    url = 'http://167.172.172.115:52353/object'
    headers = {'Content-Type': 'application/json'}
    response = None
    json = None

    def assert_response(self, expected_status_code=200):
        assert self.response is not None, "Ответ сервера отсутствует."
        assert self.response.status_code == expected_status_code, "Ошибка: Неверный статус ответа."
        assert 'id' in self.json, "Ошибка: В ответе отсутствует поле 'id'"


    def get_object_id(self):
        return self.json.get('id')
