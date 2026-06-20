import pytest
from playwright.sync_api import Playwright  # or use sync_playwright() correctly

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            channel="chrome",
            headless=False
        )

    yield browser
    browser.close()
    playwright.stop()
