import pytest
from test_api_uniquename.endpoints.create_object import CreateObject
from test_api_uniquename.endpoints.get_object import GetObject
from test_api_uniquename.endpoints.change_object import ChangeObject
from test_api_uniquename.endpoints.delete_object import DeleteObject


@pytest.fixture()
def for_object():
    return CreateObject()


@pytest.fixture()
def get_object():
    return GetObject()


@pytest.fixture()
def update():
    return ChangeObject()


@pytest.fixture()
def delete():
    return DeleteObject()


@pytest.fixture()
def create_and_delete_object():
    obj = CreateObject()
    body = {
        "name": "test_objected",
        "data": {"color": "black", "size": "big"}
    }
    obj.create_object(body)
    obj.assert_response()
    object_id = obj.get_object_id()

    yield obj, object_id

    get_obj = GetObject()
    try:
        get_obj.get_object(object_id)
        delete_obj = DeleteObject()
        delete_obj.delete_object(object_id)
        delete_obj.assert_response()
    except Exception as e:
        print(f"Ошибка при удалении объекта: {e}")
