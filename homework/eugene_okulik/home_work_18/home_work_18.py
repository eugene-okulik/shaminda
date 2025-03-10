import requests

def one_posts():
    response = requests.get('http://167.172.172.115:52353/object')
    print(response.json())
    assert response.status_code == 200, "Ошибка: Не удалось получить объекты"



def post():
    body = {
        "name": "test_object",
        "data": {
            "color": "black",
            "size": "big"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://167.172.172.115:52353/object', json=body, headers=headers)
    print(response)
    assert response.status_code == 201, "Ошибка: Не удалось создать объект"



def put():
    body = {
        "name": "test_666_object",
        "data": {
            "color": "black and black",
            "size": "big"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put('http://167.172.172.115:52353/object/585', json=body, headers=headers)
    print(response)
    assert response.status_code == 200, "Ошибка: Не удалось обновить объект"



def patch():
    body = {
        "name": "test_666_object",
        "data": {
            "size": "big"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch('http://167.172.172.115:52353/object/585', json=body, headers=headers)
    print(response)
    assert response.status_code == 200, "Ошибка: Не удалось частично обновить объект"


def delete():
    response = requests.delete('http://167.172.172.115:52353/object/585')
    print("Статус код:", response.status_code)

    if response.status_code == 204:
        print("Объект успешно удалён.")
    elif response.status_code == 200:
        print("Ответ:", response.json())
    else:
        print("Ошибка: Не удалось удалить объект. Статус код:", response.status_code)

delete()
