from playwright.sync_api import Page, expect


def test_second_by_role(page: Page):
    page.goto("https://the-internet.herokuapp.com/")
    search_form = page.get_by_role("link", name="Form Authentication")
    search_form.click()
    name_field = page.get_by_role("textbox", name="username")
    name_field.fill("username11")
    password_field = page.get_by_role("textbox", name="password")
    password_field.fill("12345qwerty")
    button_field = page.get_by_role("button", name="Login")
    button_field.click()


def test_third_by(page: Page):
    page.goto("https://demoqa.com/automation-practice-form")
    first_name = page.get_by_role("textbox", name="First Name")
    first_name.fill("daniil")
    second_name = page.get_by_role("textbox", name="Last Name")
    second_name.fill("shamin")
    email = page.get_by_placeholder("name@example.com")
    email.fill("sham@eand.com")
    gender_radiobutton = page.locator("//label[@for='gender-radio-3']")
    gender_radiobutton.check()
    mobile_number = page.get_by_placeholder("Mobile number")
    mobile_number.fill("8934345576")
    calendar = page.query_selector("#dateOfBirthInput")
    calendar.fill("29 Apr 1998")
    calendar.press("Enter")
    subjects = page.query_selector("#subjectsInput")
    subjects.fill("English")
    subjects.press("Enter")
    hobbies = page.query_selector("input[type='checkbox'][id='hobbies-checkbox-1']")
    hobbies.click()
    current_address = page.query_selector("#currentAddress")
    current_address.fill("Parish")
    state = page.query_selector("//input[@id='react-select-3-input']")
    state.fill("NCR")
    city = page.query_selector("//input[@id='city']")
    city.fill("Delhi")
    button_submit = page.locator("//button[@id='submit' and @class='btn btn-primary']")
    button_submit.click()

    expected_data = {
        "Student Name": "daniil shamin",
        "Student Email": "sham@eand.com",
        "Gender": "Other",
        "Mobile": "8934345576",
        "Date of Birth": "29 April, 1998",
        "Subjects": "English",
        "Hobbies": "Sports",
        "Address": "Parish",
        "State and City": "NCR Delhi"
    }

    table_rows = page.locator("//table[@class='table table-dark table-striped table-bordered table-hover']//tbody/tr")
    actual_data = {}

    for row in table_rows.element_handles():
        key = row.locator("td:nth-of-type(1)").inner_text()
        value = row.locator("td:nth-of-type(2)").inner_text()
        actual_data[key] = value

    for key, expected_value in expected_data.items():
        actual_value = actual_data.get(key)
        assert actual_value == expected_value, f"Mismatch for {key}: expected '{expected_value}', got '{actual_value}'"

    close_button = page.get_by_role("button", name="Close")
    close_button.click()
