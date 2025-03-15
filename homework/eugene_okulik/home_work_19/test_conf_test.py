import requests
import pytest

BASE_URL = 'http://167.172.172.115:52353/object'

@pytest.fixture
def create_object():
    body = {
        "name": "test_object",
        "data": {
            "color": "black",
            "size": "big"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(BASE_URL, json=body, headers=headers)

    print(f"Create object response: {response.status_code} - {response.text}")

    if response.status_code == 201:
        object_id = response.json().get('id')
        yield object_id
    elif response.status_code == 200:
        print("Объект уже существует или был успешно создан, но возвращён статус 200.")
        object_id = response.json().get('id')
        yield object_id
    else:
        raise AssertionError(
            f"Ошибка: Не удалось создать объект. Статус: {response.status_code}, Ответ: {response.text}"
        )

    delete_response = requests.delete(f'{BASE_URL}/{object_id}')
    assert delete_response.status_code in [204, 200], "Ошибка: Не удалось удалить объект"

