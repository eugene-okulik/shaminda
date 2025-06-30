from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_one(driver):
    driver.get("https://www.demoblaze.com/index.html")
    driver.execute_script("window.open('https://www.demoblaze.com/prod.html?idp_=1', '_blank');")
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element(By.XPATH,
                        "//div[@class='col-sm-12 col-md-6 col-lg-6']/a[@onclick='addToCart(1)']").click()

    alert = driver.switch_to.alert
    alert.accept()

    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.find_element(By.XPATH, "//a[@id='cartur' and @class='nav-link']").click()

    text_add = driver.find_element(By.XPATH, "//td[text()='Samsung galaxy s6']")
    assert text_add.text == "Samsung galaxy s6"
