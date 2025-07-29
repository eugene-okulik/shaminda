from test_UI_unique_name.base.base_page import BasePage


class RegistrationPage(BasePage):
    _PAGE_URL = 'https://magento.softwaretestingboard.com/customer/account/create/'

    _FIRST_NAME = "//input[@id='firstname' and contains(@class, 'input-text')]"
    _LAST_NAME = "//input[@id='lastname' and contains(@class, 'input-text')]"
    _EMAIL = "//input[@id='email_address' and contains(@class, 'input-text')]"
    _PASSWORD = "//input[@id='password' and contains(@class, 'input-text')]"
    _CONFIRM_PASSWORD = "//input[@id='password-confirmation' and contains(@class, 'input-text')]"
    _BUTTON_CONFIRM = (
        "//button[contains(@class, 'action submit primary')"
        " and @title='Create an Account']"
    )
    _TEXT_SUCSSES_CREATE_ACCOUNT = (
        "//div[contains(text(), 'Thank you for registering with Main Website Store.')]"
    )
    _PASSWORD_STRENGHTH_WEAK = (
        "//div[@id='password-strength-meter' and contains(., 'Weak')]"
    )
    _ENTER_VALUE_AGAIN = (
        "//div[@id='password-confirmation-error' and contains(text(), 'Please enter the same value again.')]"
    )

    def input_firstname(self, firstname):
        self.input_text(self._FIRST_NAME, firstname)

    def input_lastname(self, lastname):
        self.input_text(self._LAST_NAME, lastname)

    def input_email(self, email):
        self.input_text(self._EMAIL, email)

    def input_password(self, password):
        self.input_text(self._PASSWORD, password)

    def input_confirm_password(self, confirm_password):
        self.input_text(self._CONFIRM_PASSWORD, confirm_password)

    def click_button_confirm(self):
        self.click_element(self._BUTTON_CONFIRM)

    def text_sucsses_create(self):
        return self.find_element(self._TEXT_SUCSSES_CREATE_ACCOUNT).inner_text()

    def password_strength_weak(self):
        return self.find_element(self._PASSWORD_STRENGHTH_WEAK).inner_text()

    def enter_value_again(self):
        return self.find_element(self._ENTER_VALUE_AGAIN).inner_text()
