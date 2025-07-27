import allure

@allure.feature("тесты регистрации пользователя")
class TestRegistration:
    @allure.title("Регистрируемся(позитивный тест)")
    def test_registration(self, registration):
        with allure.step("открываем страницу регистрации"):
            registration.open()
        with allure.step("вводим имя"):
            registration.input_firstname('daniil')
        with allure.step("вводим фамилию"):
            registration.input_lastname('shamin')
        with allure.step("Вводим почту"):
            registration.input_email('shamin@yan.ru')
        with allure.step("Вводим пароль"):
            registration.input_password('Qwerty12345')
        with allure.step("Вводим пароль повторно"):
            registration.input_confirm_password('Qwerty12345')
        with allure.step("Нажимаем кнопку: 'create account'"):
            registration.click_button_confirm()
        with allure.step("аккаунт успешно создан"):
            success_message = registration.text_sucsses_create()
            expected_message = "Thank you for registering with Main Website Store."
            assert success_message == expected_message, (f"Ожидалось: '{expected_message}',было: '{success_message}'")

    @allure.title("Регистрируемся(негативный тест Password Strength: Weak)")
    def test_registration_negativ(self, registration):
        with allure.step("открываем страницу регистрации"):
            registration.open()
        with allure.step("вводим имя"):
            registration.input_firstname('daniil')
        with allure.step("вводим фамилию"):
            registration.input_lastname('shamin')
        with allure.step("Вводим почту"):
            registration.input_email('shamin@yan.ru')
        with allure.step("Вводим пароль"):
            registration.input_password('qwerty12345')
        with allure.step("Вводим пароль повторно"):
            registration.input_confirm_password('qwerty12345')
        with allure.step("Нажимаем кнопку: 'create account'"):
            registration.click_button_confirm()
        with allure.step("слабый пароль"):
            success_message = registration.password_strength_weak()
            expected_message = "Weak"
            assert success_message == expected_message, (f"Ожидалось: '{expected_message}',было: '{success_message}'")

    @allure.title("Регистрируемся(негативный тест Please enter the same value again)")
    def test_registration_enter_value_again(self, registration):
        with allure.step("открываем страницу регистрации"):
            registration.open()
        with allure.step("вводим имя"):
            registration.input_firstname('daniil')
        with allure.step("вводим фамилию"):
            registration.input_lastname('shamin')
        with allure.step("Вводим почту"):
            registration.input_email('shamin@yan.ru')
        with allure.step("Вводим пароль"):
            registration.input_password('Qwerty12345')
        with allure.step("Вводим пароль повторно"):
            registration.input_confirm_password('qwerty1234')
        with allure.step("Нажимаем кнопку: 'create account'"):
            registration.click_button_confirm()
        with allure.step("введите пароль еще раз"):
            success_message = registration.enter_value_again()
            expected_message = "Please enter the same value again."
            assert success_message == expected_message, (f"Ожидалось: '{expected_message}',было: '{success_message}'")
