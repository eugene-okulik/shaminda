import pytest
from test_api_uniquename.endpoints.create_post import CreatePost
from test_api_uniquename.endpoints.to_change_post import ChangePost
from test_api_uniquename.endpoints.delete_post import DeleteObject


@pytest.fixture()
def for_post():
    return CreatePost()


@pytest.fixture()
def update():
    return ChangePost()


@pytest.fixture()
def delete():
    return DeleteObject()
