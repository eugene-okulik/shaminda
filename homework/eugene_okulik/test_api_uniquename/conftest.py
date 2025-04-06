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
