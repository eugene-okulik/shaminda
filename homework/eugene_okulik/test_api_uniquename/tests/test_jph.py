import pytest
from test_api_uniquename.endpoints.creat_post import CreatPost
from test_api_uniquename.endpoints.delete_post import DeleteObject
from test_api_uniquename.endpoints.to_change_post import ChangePost

TEST_DATA = [
    {"color": "black", "size": "big"},
    {"color": "white", "size": "mini"},
    {"color": "red", "size": "xxl"}
]


@pytest.mark.parametrize('data', TEST_DATA)
def test_create_object(data):
    body = {
        "name": "test_objected",
        "data": data
    }
    post_creator = CreatPost()
    post_creator.new_post(body)
    post_creator.assertions_message()
    print("Тест прошел успешно.")


def test_change_object():
    post_creator = CreatPost()
    body = {
        "name": "test_objected",
        "data": {"color": "rrrr", "size": "smal"}
    }
    post_creator.new_post(body)
    post_creator.assertions_message()
    object_id = post_creator.get_object_id()

    post_change = ChangePost()
    post_change.check_object_exists(object_id)

    update_body = {
        "name": "updated_objected",
        "data": {"color": "blue", "size": "large"}
    }
    post_change.new_post(object_id, update_body)
    post_change.assertions_message()
    print("Тест прошел успешно.")


def test_delete_object():
    post_creator = CreatPost()
    body = {
        "name": "test_objected",
        "data": {"color": "black", "size": "big"}
    }
    post_creator.new_post(body)
    post_creator.assertions_message()
    object_id = post_creator.get_object_id()

    delete_post = DeleteObject()
    delete_post.delete_obj(object_id)
    delete_post.assertions_message()

    if delete_post.check_object_deleted(object_id):
        print("Объект успешно удален.")
    else:
        print("Объект все еще существует, удаление не удалось.")
