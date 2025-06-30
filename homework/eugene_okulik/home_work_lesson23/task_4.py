from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver_with_browser_2():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_start(driver_with_browser_2):
    driver_with_browser_2.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    button = driver_with_browser_2.find_element(By.XPATH, "//button[text()='Start']")
    button.click()

    WebDriverWait(driver_with_browser_2, 15).until(
        EC.visibility_of_element_located((By.ID, "finish"))
    )

    finish_text = driver_with_browser_2.find_element(By.ID, "finish").text
    assert finish_text == "Hello World!", (
        f"Test failed: expected 'Hello World!', got '{finish_text}'"
    )
