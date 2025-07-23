from playwright.sync_api import Page, expect


def test_alert(page: Page):
    page.goto("https://www.qa-practice.com/elements/alert/confirm#")
    button_click = page.locator(".a-button")
    button_click.click()
    dialog = page.wait_for_event("dialog")
    print(f"Dialog message: {dialog.message}")
    dialog.accept()
    result_element = page.locator("#result-text")
    result_text = result_element.text_content()
    expect(result_text).to_be("Ok")

def test_new_tab_navigation(page: Page):
    page.goto("https://www.qa-practice.com/elements/new_tab/button")
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="Click").click()
    page1 = page1_info.value
    page1.wait_for_load_state("load")
    result_text = page1.locator("#result-text")
    expect(result_text).to_be_visible()
    expect(result_text.inner_text()).to_be("I am a new page in a new tab")
    page1.close()
    page.go_back()
    page.wait_for_load_state("load")
    new_page_button = page.locator("#new-page-button")
    expect(new_page_button).to_be_enabled()


def test_color(page: Page):
    page.goto("https://demoqa.com/dynamic-properties", timeout=60000)
    color_change_button = page.locator("#colorChange")
    color_change_button.wait_for(state="visible")
    color_change_button.click()
    page.wait_for_timeout(6000)
    expect(color_change_button).to_have_css("background-color", "rgb(0, 105, 217)")
