import json
from playwright.sync_api import Page, expect


def test_request_replace(page: Page):
    def handle_response(route):
        data = route.fetch().json()
        data['body']['digitalMat'][0]['familyTypes'][0]['productName'] = 'яблокофон 16 про'
        route.fulfill(body=json.dumps(data))

    page.route("**/digitalmat", handle_response)
    page.goto('https://www.apple.com/shop/buy-iphone')
    page.get_by_role("heading", name="iPhone 16 Pro & iPhone 16 Pro").click()

    expect(page.get_by_role("heading", name="яблокофон 16 про")).to_have_text("яблокофон 16 про")
