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
        EC.visibility_of_element_located((By.XPATH, "//img[@class='product-image-photo'"
                                                    " and @alt='Push It Messenger Bag']"))
    )

    ActionChains(driver).move_to_element(first_product).perform()
    add_to_compare_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='action tocompare' and @title='Add to Compare']"))
    )
    add_to_compare_button.click()
    compare_section = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH,
                                          "//strong[@id='block-compare-heading' and text()='Compare Products']"))
    )

    compare_products = compare_section.find_elements(By.XPATH,
                                                     "//li[contains(@class,"
                                                     " 'product-item')]//a[text()='Push It Messenger Bag']")

    assert len(compare_products) > 0, "Product 'Push It Messenger Bag' not found in compare list."

    assert compare_products[0].text == "Push It Messenger Bag", "Product name does not match."
# без впн не открывает сайт, под впн выпадает какая то реклама которой нет при запуске просто в браузере
# пытался как то воспроизвести рекламу в браузере не вышло,тест как пройти понимаю но реклама не дает
