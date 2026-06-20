def test_google(browser):
    page = browser.new_page()
    page.goto("https://www.google.com")
    print(page.title())
    assert "Google" in page.title()
    page.locator("[name=q]").fill("hello")
    page.keyboard.press("Enter")
    page.wait_for_timeout(10000)
    print(page.title())
