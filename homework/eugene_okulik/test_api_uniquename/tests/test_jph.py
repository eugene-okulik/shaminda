import pytest

@pytest.mark.parametrize('data', [
    {"color": "black", "size": "big"},
    {"color": "white", "size": "mini"},
    {"color": "red", "size": "xxl"}
])
def test_create_object(for_post, data):
    body = {
        "name": "test_objected",
        "data": data
    }
    for_post.create_object(body)
    for_post.assert_response()
    print("Тест прошел успешно.")


def test_change_object(for_post, update):
    body = {
        "name": "test_objected",
        "data": {"color": "rrrr", "size": "smal"}
    }
    for_post.create_object(body)
    for_post.assert_response()
    object_id = for_post.get_object_id()

    update.check_object_exists(object_id)

    update_body = {
        "name": "updated_objected",
        "data": {"color": "blue", "size": "large"}
    }
    update.update_object(object_id, update_body)
    update.assert_response()
    print("Тест прошел успешно.")


def test_patch_object(for_post, update):
    body = {
        "name": "test_objected",
        "data": {"color": "green"}
    }
    for_post.create_object(body)
    for_post.assert_response()
    object_id = for_post.get_object_id()

    update.check_object_exists(object_id)

    patch_body = {
        "data": {"size": "medium"}  # Обновляем только размер
    }
    update.patch_object(object_id, patch_body)
    update.assert_response()
    print("Частичное обновление прошло успешно.")


def test_delete_object(for_post, delete):
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
