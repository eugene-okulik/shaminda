import allure


@allure.feature("Тесты раздела Sale")
class TestSale:
    @allure.title("выбираем товар, добавляем его в раздел сравнений")
    def test_shopping(self, sale):
        with allure.step("открываем страницу выбора товара"):
            sale.open()
        with allure.step("выбираем товар"):
            sale.choise_tshort()
        with allure.step("выбираем размер"):
            sale.choose_size_s()
        with allure.step("выбираем цвет"):
            sale.choose_color_yellow()
        with allure.step("нажимаем кнопку добавить в сравнение"):
            sale.click_clear_compaire()
        with allure.step("проверяем что товар добавился"):
            quantity = sale.item_list()
            assert quantity >= 1

    @allure.title("очищаем список сравнения")
    def test_clear_compair(self, sale):
        with allure.step("открываем страницу выбора товара"):
            sale.open()
        with allure.step("выбираем товар"):
            sale.choise_tshort()
        with allure.step("выбираем размер"):
            sale.choose_size_s()
        with allure.step("выбираем цвет"):
            sale.choose_color_yellow()
        with allure.step("нажимаем кнопку добавить в сравнение"):
            sale.click_clear_compaire()
        with allure.step("проверяем что товар добавился"):
            sale.item_list()
        with allure.step("очищаем список"):
            sale.click_clear_compair()

    @allure.title("добавляем товар в корзину")
    def test_add_to_cart(self, sale):
        with allure.step("открываем страницу выбора товара"):
            sale.open()
        with allure.step("выбираем товар"):
            sale.choise_tshort()
        with allure.step("выбираем размер"):
            sale.choose_size_s()
        with allure.step("выбираем цвет"):
            sale.choose_color_yellow()
        with allure.step("добавляем товар в корзину"):
            sale.click_add_to_cart()
        with allure.step("проверяем что товар появился в корзине"):
            cart = sale.cart_changed()
            assert len(cart) >= 1
