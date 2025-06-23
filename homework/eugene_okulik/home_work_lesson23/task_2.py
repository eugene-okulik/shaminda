from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from time import sleep


@pytest.fixture
def driver_with_browser_2():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    sleep(5)


def test_second(driver_with_browser_2):
    driver_with_browser_2.get("https://demoqa.com/automation-practice-form")

    input_1 = driver_with_browser_2.find_element(By.XPATH, "//input[@id='firstName' and @type='text']")
    input_1.send_keys("Daniil")

    input_2 = driver_with_browser_2.find_element(By.XPATH, "//input[@id='lastName' and @type='text']")
    input_2.send_keys("Shamin")

    input_3 = driver_with_browser_2.find_element(By.XPATH, "//input[@id='userEmail' and @type='text']")
    input_3.send_keys("shamin@yandex.ru")

    input_4_label = driver_with_browser_2.find_element(By.XPATH, "//label[@for='gender-radio-1']")
    input_4_label.click()

    input_5 = driver_with_browser_2.find_element(By.XPATH, "//input[@id='userNumber' and @type='text']")
    input_5.send_keys("1234567891")

    input_6 = driver_with_browser_2.find_element(By.XPATH, "//input[@id='dateOfBirthInput' and @type='text']")
    input_6.click()

    select = Select(driver_with_browser_2.find_element(By.XPATH, "//select[@class='react-datepicker__month-select']"))
    select.select_by_visible_text("April")

    select_year = Select(
        driver_with_browser_2.find_element(By.XPATH, "//select[@class='react-datepicker__year-select']"))
    select_year.select_by_visible_text("1998")

    day_choice = driver_with_browser_2.find_element(By.XPATH,
                                                    "//div[@class='react-datepicker__day react-datepicker__day--029' and text()='29']")
    day_choice.click()

    input_7 = driver_with_browser_2.find_element(By.ID, "subjectsInput")
    input_7.click()
    input_7.send_keys("English")
    sleep(5)
    input_7.send_keys(Keys.ENTER)
    sleep(5)

    input_8 = driver_with_browser_2.find_element(By.XPATH, "//label[@class='custom-control-label' and text()='Music']")
    input_8.click()

    input_9 = driver_with_browser_2.find_element(By.XPATH, "//textarea[@placeholder='Current Address']")
    input_9.send_keys("I am from Russia")

    input_10 = driver_with_browser_2.find_element(By.XPATH, "//div[@id='state']")
    input_10.click()

    input_11 = driver_with_browser_2.find_element(By.XPATH, "//input[@id='react-select-3-input']")
    input_11.send_keys("NCR")
    input_11.send_keys(Keys.ENTER)

    input_12 = driver_with_browser_2.find_element(By.XPATH, "//div[@id='city']")
    input_12.click()

    input_13 = driver_with_browser_2.find_element(By.XPATH, "//input[@id='react-select-4-input']")
    input_13.send_keys("Delhi")
    input_13.send_keys(Keys.ENTER)

    input_14 = driver_with_browser_2.find_element(By.XPATH, "//button[@id='submit' and @class='btn btn-primary']")
    input_14.click()

    WebDriverWait(driver_with_browser_2, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "modal-content"))
    )

    expected_data = {
        "Student Name": "Daniil Shamin",
        "Student Email": "shamin@yandex.ru",
        "Gender": "Male",
        "Mobile": "1234567891",
        "Date of Birth": "29 April,1998",
        "Subjects": "English",
        "Hobbies": "Music",
        "Address": "I am from Russia",
        "State and City": "NCR Delhi"
    }

    table_rows = driver_with_browser_2.find_elements(By.XPATH,
                                                     "//table[@class='table table-dark table-striped table-bordered table-hover']//tbody/tr")
    actual_data = {}

    for row in table_rows:
        key = row.find_element(By.XPATH, "td[1]").text
        value = row.find_element(By.XPATH, "td[2]").text
        actual_data[key] = value

    for key, expected_value in expected_data.items():
        actual_value = actual_data.get(key)
        assert actual_value == expected_value, f"Mismatch for {key}: expected '{expected_value}', got '{actual_value}'"

    close_button = driver_with_browser_2.find_element(By.ID, "closeLargeModal")
    close_button.click()
