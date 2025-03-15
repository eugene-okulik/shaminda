import pytest
import requests
import allure

BASE_URL = 'http://167.172.172.115:52353/object'


@pytest.fixture(scope="session")
def setup_session():
    print("Start testing")
    yield
    print("Testing completed")


@pytest.fixture
def setup_teardown():
    print("before test")
    yield
    print("after test")


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


@pytest.mark.parametrize("object_data", [
    {"name": "test_object_1", "data": {"color": "red", "size": "small"}},
    {"name": "test_object_2", "data": {"color": "blue", "size": "medium"}},
    {"name": "test_object_3", "data": {"color": "green", "size": "large"}}
])
@allure.feature('Object Creation')
@allure.story('Create multiple objects')
def test_create_objects(object_data, setup_session, setup_teardown):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(BASE_URL, json=object_data, headers=headers)

    print(f"Create objects response for {object_data}: {response.status_code} - {response.text}")

    if response.status_code == 201:
        assert True
    elif response.status_code == 200:
        print("Объект уже существует или был успешно создан, но возвращён статус 200.")
        assert True
    else:
        assert False, f"Ошибка: Не удалось создать объект. Статус: {response.status_code}, Ответ: {response.text}"


@pytest.mark.critical
@allure.feature('Object Update')
@allure.story('Update an object')
def test_update_object(create_object, setup_session, setup_teardown):
    object_id = create_object
    body = {
        "name": "updated_object",
        "data": {
            "color": "yellow",
            "size": "small"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(f'{BASE_URL}/{object_id}', json=body, headers=headers)

    print(f"Update object response: {response.status_code} - {response.text}")

    assert response.status_code == 200, "Ошибка: Не удалось обновить объект"


@pytest.mark.medium
@allure.feature('Object Update')
@allure.story('Partial update of an object')
def test_partial_update_object(create_object, setup_session, setup_teardown):
    object_id = create_object
    body = {
        "data": {
            "size": "extra large"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(f'{BASE_URL}/{object_id}', json=body, headers=headers)

    print(f"Partial update response: {response.status_code} - {response.text}")

    assert response.status_code == 200, "Ошибка: Не удалось частично обновить объект"


@allure.feature('Object Retrieval')
@allure.story('Get an object')
def test_get_object(create_object, setup_session, setup_teardown):
    object_id = create_object
    response = requests.get(f'{BASE_URL}/{object_id}')

    print(f"Get object response: {response.status_code} - {response.text}")

    assert response.status_code == 200, "Ошибка: Не удалось получить объект"


@allure.feature('Object Deletion')
@allure.story('Delete an object')
def test_delete_object(create_object, setup_session, setup_teardown):
    object_id = create_object
    response = requests.delete(f'{BASE_URL}/{object_id}')

    print(f"Delete object response: {response.status_code} - {response.text}")

    assert response.status_code in [204, 200], "Ошибка: Не удалось удалить объект"