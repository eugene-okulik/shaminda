import allure


@allure.feature("Выбираем товар на странице eco-friendly ")
class TestChoiseShmot:

    @allure.title("выбираем товар, добавляем его в раздел сравнений")
    def test_shopping(self, eco_friendly):
        with allure.step("открываем страницу выбора товара"):
            eco_friendly.open()
        with allure.step("нажимаем кнопку перехода на следующую страницу"):
            eco_friendly.click_next()
        with allure.step("выбираем товар"):
            eco_friendly.acction_choose()
        with allure.step("выбираем размер"):
            eco_friendly.click_choose_size_xl()
        with allure.step("выбираем цвет"):
            eco_friendly.click_choose_color_purple()
        with allure.step("нажимаем кнопку добавить в сравнение"):
            eco_friendly.click_compair()
        with allure.step("проверяем что товар добавился"):
            count = eco_friendly.item_list()
            assert count > 0

    @allure.title("очищаем список сравнения")
    def test_clear_compair(self, eco_friendly):
        with allure.step("открываем страницу выбора товара"):
            eco_friendly.open()
        with allure.step("нажимаем кнопку перехода на следующую страницу"):
            eco_friendly.click_next()
        with allure.step("выбираем товар"):
            eco_friendly.acction_choose()
        with allure.step("выбираем размер"):
            eco_friendly.click_choose_size_xl()
        with allure.step("выбираем цвет"):
            eco_friendly.click_choose_color_purple()
        with allure.step("нажимаем кнопку добавить в сравнение"):
            eco_friendly.click_compair()
        with allure.step("проверяем что товар добавился"):
            count = eco_friendly.item_list()
            assert count > 0
        with allure.step("очищаем список"):
            eco_friendly.click_clear_compair()

    @allure.title("добавляем товар в корзину")
    def test_add_to_cart(self, eco_friendly):
        with allure.step("открываем страницу выбора товара"):
            eco_friendly.open()
        with allure.step("нажимаем кнопку перехода на следующую страницу"):
            eco_friendly.click_next()
        with allure.step("выбираем товар"):
            eco_friendly.acction_choose()
        with allure.step("выбираем размер"):
            eco_friendly.click_choose_size_xl()
        with allure.step("выбираем цвет"):
            eco_friendly.click_choose_color_purple()
        with allure.step("добавляем товар в корзину"):
            eco_friendly.click_add_to_cart()
        with allure.step("проверяем что товар появился в корзине"):
            count = eco_friendly.get_cart_items_count()
            assert count > 0
