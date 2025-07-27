

class BasePage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto(self._PAGE_URL)

    def find_element(self, locator):
        return self.page.locator(locator)

    def click_element(self, locator):
        self.page.locator(locator).click()

    def input_text(self, locator, text):
        el = self.page.locator(locator)
        el.fill(text)

    def attach_screenshot(self, name="screenshot"):
        import allure
        allure.attach(self.page.screenshot(), name=name, attachment_type=allure.attachment_type.PNG)

    def action_choose(self, locator):
        self.page.locator(locator).hover()
