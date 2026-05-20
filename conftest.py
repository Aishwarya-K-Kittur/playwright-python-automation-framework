import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
import os

BASE_URL = "https://www.saucedemo.com/"

def pytest_addoption(parser):

    parser.addoption(
        "--browser",
        action="store",
        default="chromium",
        help="Browser selection"
    )

# @pytest.fixture(params=["chromium", "firefox", "webkit"])
@pytest.fixture(params=["chromium"])
def page(request):

    with sync_playwright() as p:

        browser_name = request.config.getoption(
            "--browser"
        )
        browser = getattr(p, browser_name).launch(
            headless=False,
            slow_mo=100,
        )
        context = browser.new_context()
        context.tracing.start(
            screenshots=True,
            snapshots=True,
            sources=True
        )
        page = context.new_page()
        page.goto(BASE_URL)

        yield page

        context.tracing.stop(
            path="trace.zip"
        )

        context.close()
        browser.close()

@pytest.fixture
def logged_in_page(page):

    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    yield page

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            os.makedirs(
                "screenshots",
                exist_ok=True
            )
            screenshot_path = (
                f"screenshots/{item.name}.png"
            )
            page.screenshot(
                path=screenshot_path
            )
            print(
                f"Screenshot saved: {screenshot_path}"
            )