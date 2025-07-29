import allure


@allure.feature("тесты регистрации пользователя")
class TestRegistration:

    def check_result(self, actual, expected):
        assert actual == expected, f"Ожидалось: '{expected}', было: '{actual}'"

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
            actual = registration.text_sucsses_create()
            expected = "Thank you for registering with Main Website Store."
            self.check_result(actual, expected)

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
            actual = registration.password_strength_weak()
            expected = "Weak"
            self.check_result(actual, expected)

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
            actual = registration.enter_value_again()
            expected = "Please enter the same value again."
            self.check_result(actual, expected)
