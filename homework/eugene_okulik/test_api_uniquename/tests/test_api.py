
from test_api_uniquename.endpoints.get_object import GetObject
from test_api_uniquename.endpoints.delete_object import DeleteObject


def test_create_object(create_and_delete_object):
    _, object_id = create_and_delete_object

    get_obj = GetObject()
    retrieved_object = get_obj.get_object(object_id)
    assert retrieved_object is not None, "Ошибка: Объект не был найден."
    print("Тест прошел успешно.")


def test_change_object(create_and_delete_object, update):
    _, object_id = create_and_delete_object

    update_body = {
        "name": "updated_objected",
        "data": {"color": "blue", "size": "large"}
    }
    update.update_object(object_id, update_body)
    update.assert_response()
    print("Тест прошел успешно.")


def test_patch_object(create_and_delete_object, update):
    _, object_id = create_and_delete_object

    patch_body = {
        "data": {"size": "medium"}
    }
    update.patch_object(object_id, patch_body)
    update.assert_response()
    print("Частичное обновление прошло успешно.")


def test_delete_object(create_and_delete_object):
    _, object_id = create_and_delete_object

    delete_obj = DeleteObject()
    delete_obj.delete_object(object_id)
