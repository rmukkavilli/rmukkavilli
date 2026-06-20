import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser():
    is_ci = os.getenv('CI', "false").tolower() = "true"
    with sync_playwright() as p:
        if is_ci:
            browser = p.chromium.launch(headless=True)
        else:
            browser = p.chromium.launch(channel="chrome", headless=False)
        yield browser