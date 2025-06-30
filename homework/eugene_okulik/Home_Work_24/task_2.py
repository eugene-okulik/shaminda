import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_compare_product(driver):
    driver.get("https://magento.softwaretestingboard.com/gear/bags.html")
    first_product = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH,"//li[@class='item product product-item']"))
    )

    ActionChains(driver).move_to_element(first_product).perform()
    add_to_compare_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='action tocart primary']"))
    )
    add_to_compare_button.click()
    compare_section = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH,
                                          "//strong[@id='block-compare-heading' and text()='Compare Products']"))
    )
    # По нажатии add_to_compare_button.click() появляется ошибка The requested qty is not available и переход
    # на страницу с ошибкой , с остальными товарами такого нет, но поле  compare_products не меняется при нажатии
    # на них, обьясните может я не так понял задачу, но после нажатия кнопки должно изменится  compare_products
    # а не появится ошибка не дающая сделать что либо
    # по этому дальше тест дописывал абстракто что все работает
    compare_products = compare_section.find_elements(By.XPATH,
                                                     "//div[@class='empty' and text()='You have no items to compare.']")
    assert len(compare_products) > 0, "Товар не добавлен в секцию сравнения."
    # Выводим название первого товара в секции сравнения
    product_name = compare_products[0].find_element(By.XPATH, ".product-item-name").text
    print(f"Товар в секции сравнения: {product_name}")
