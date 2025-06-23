from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
import pytest


@pytest.fixture
def driver_with_browser_2():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    sleep(5)


def test_first(driver_with_browser_2):
    driver_with_browser_2.get("https://www.qa-practice.com/elements/select/single_select")

    select = Select(driver_with_browser_2.find_element(By.ID, "id_choose_language"))
    select.select_by_value("1")

    submit = driver_with_browser_2.find_element(By.ID, "submit-id-submit")
    submit.click()

    result = driver_with_browser_2.find_element(By.XPATH, "//p[@id='result-text']")
    assert result.text == "Python"
