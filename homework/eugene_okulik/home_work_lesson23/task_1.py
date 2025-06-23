from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import pytest

@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    sleep(3)

def test_first(driver):
    input_data = 'ctoto'
    sleep(3)
    driver.get('https://www.qa-practice.com/elements/input/simple')
    sleep(3)
    text_string = driver.find_element(By.ID, "id_text_string")
    sleep(3)
    text_string.send_keys(input_data)
    sleep(3)
    text_string.send_keys(Keys.ENTER)
    result_text = driver.find_element(By.ID, "result-text")
    assert result_text.text == input_data, "not found"
    print(result_text.text)
