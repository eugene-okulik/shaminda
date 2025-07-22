from playwright.sync_api import Page,expect



def test_alert(page: Page):
    page.goto("https://www.qa-practice.com/elements/alert/confirm#")
    button_click = page.locator(".a-button")
    button_click.click()
    dialog = page.wait_for_event("dialog")
    print(f"Dialog message: {dialog.message}")
    dialog.accept()
    result_element = page.locator("#result-text")
    result_text = result_element.text_content()
    assert result_text == "Ok", f"Expected 'Ok', but got '{result_text}'"


def test_new_tab_navigation(page: Page):
    page.goto("https://www.qa-practice.com/elements/new_tab/button")

    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="Click").click()

    page1 = page1_info.value
    page1.wait_for_load_state("load")
    result_text = page1.locator("#result-text")
    assert result_text.is_visible(), "Element with text 'I am a new page in a new tab' is not visible"

    assert result_text.inner_text() == "I am a new page in a new tab", "Text does not match"
    page1.close()
    page.go_back()
    page.wait_for_load_state("load")
    new_page_button = page.locator("#new-page-button")
    assert new_page_button.is_enabled(), "Element 'Click' is not enabled"


def test_color(page: Page):
    page.goto("https://demoqa.com/dynamic-properties")
    color_change_button = page.locator("#colorChange")
    color_change_button.wait_for(state="visible")
    color_change_button.click()
    page.wait_for_timeout(6000)
    button_color = color_change_button.evaluate("element => window.getComputedStyle(element).backgroundColor")
    assert button_color == "rgb(0, 105, 217)", f"Expected color 'rgb(0, 105, 217)', but got '{button_color}'"
