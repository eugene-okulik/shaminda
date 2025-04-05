import pytest
from test_api_uniquename.endpoints.create_post import CreatePost
from test_api_uniquename.endpoints.get_post import GetPost
from test_api_uniquename.endpoints.to_change_post import ChangePost
from test_api_uniquename.endpoints.delete_post import DeleteObject


@pytest.fixture()
def for_post():
    return CreatePost()


@pytest.fixture()
def get_post():
    return GetPost()


@pytest.fixture()
def update():
    return ChangePost()


@pytest.fixture()
def delete():
    return DeleteObject()


def test_create_object(for_post):
    body = {
        "name": "test_objected",
        "data": {"color": "black", "size": "big"}
    }
    for_post.create_object(body)
    for_post.assert_response()
    print("Тест прошел успешно.")


def test_change_object(for_post, update, get_post):
    body = {
        "name": "test_objected",
        "data": {"color": "rrrr", "size": "smal"}
    }
    for_post.create_object(body)
    for_post.assert_response()
    object_id = for_post.get_object_id()

    get_post.check_object_exists(object_id)

    update_body = {
        "name": "updated_objected",
        "data": {"color": "blue", "size": "large"}
    }
    update.update_object(object_id, update_body)
    update.assert_response()
    print("Тест прошел успешно.")


def test_patch_object(for_post, update, get_post):
    body = {
        "name": "test_objected",
        "data": {"color": "green"}
    }
    for_post.create_object(body)
    for_post.assert_response()
    object_id = for_post.get_object_id()

    get_post.check_object_exists(object_id)

    patch_body = {
        "data": {"size": "medium"}  # Обновляем только размер
    }
    update.patch_object(object_id, patch_body)
    update.assert_response()
    print("Частичное обновление прошло успешно.")


def test_delete_object(for_post, delete, get_post):
    body = {
        "name": "test_objected",
        "data": {"color": "black", "size": "big"}
    }
    for_post.create_object(body)
    for_post.assert_response()
    object_id = for_post.get_object_id()

    delete.delete_object(object_id)
    delete.assert_response()

    if delete.check_object_deleted(object_id):
        print("Объект успешно удален.")
    else:
        print("Объект все еще существует, удаление не удалось.")
