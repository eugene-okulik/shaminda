import pytest


def test_create_object(for_object):
    body = {
        "name": "test_objected",
        "data": {"color": "black", "size": "big"}
    }
    for_object.create_object(body)
    for_object.assert_response()
    print("Тест прошел успешно.")


def test_change_object(for_object, update, get_object):
    body = {
        "name": "test_objected",
        "data": {"color": "rrrr", "size": "smal"}
    }
    for_object.create_object(body)
    for_object.assert_response()
    object_id = for_object.get_object_id()

    get_object.get_object(object_id)

    update_body = {
        "name": "updated_objected",
        "data": {"color": "blue", "size": "large"}
    }
    update.update_object(object_id, update_body)
    update.assert_response()
    print("Тест прошел успешно.")


def test_patch_object(for_object, update, get_object):
    body = {
        "name": "test_objected",
        "data": {"color": "green"}
    }
    for_object.create_object(body)
    for_object.assert_response()
    object_id = for_object.get_object_id()

    patch_body = {
        "data": {"size": "medium"}  # Обновляем только размер
    }
    update.patch_object(object_id, patch_body)
    update.assert_response()
    print("Частичное обновление прошло успешно.")


def test_delete_object(for_object, delete, get_object):
    body = {
        "name": "test_objected",
        "data": {"color": "black", "size": "big"}
    }
    for_object.create_object(body)
    for_object.assert_response()
    object_id = for_object.get_object_id()

    delete.delete_object(object_id)
    delete.assert_response()

    print("Объект успешно удален.")
