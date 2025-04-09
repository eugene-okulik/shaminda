from locust import task, HttpUser


class PlaceHolder(HttpUser):
    @task(1)
    def get_list_user(self):
        self.client.get('/api/users?page=2')

    @task(3)
    def post_user(self):
        data = {
            'name': 'Piter Parker',
            'job': 'Spider man'
        }
        response = self.client.post('/api/users', json=data)
        assert response.status_code == 201, f"Ошибка при создании пользователя: {response.text}"

    @task(2)
    def patch_user(self):
        data = {
            'name': 'Piter Parker',
            'job': 'Venom'
        }
        response = self.client.patch('/api/users/2', json=data)
        assert response.status_code == 200, f"Ошибка при обновлении пользователя: {response.text}"
        assert 'updatedAt' in response.json(), "Пользователь не обновился частично"

    @task(4)
    def delete_user(self):
        response = self.client.delete('/api/users/2')
        assert response.status_code == 204, f'Ошибка при удалении юзера:{response.text}'
