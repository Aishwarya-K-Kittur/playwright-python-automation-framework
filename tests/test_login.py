import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize(
    "username,password",
    [
        ("standard_user", "secret_sauce"),
        ("problem_user", "secret_sauce"),
        ("performance_glitch_user", "secret_sauce")
    ]
)

def test_login(username, password, page):
    login_page = LoginPage(page)
    login_page.login(username, password)
    assert "inventory" in page.url

@pytest.mark.parametrize(
    "username,password,error_message",
    [
        ("locked_out_user", "secret_sauce", "Epic sadface"),
        ("invalid", "invalid", "Epic sadface")
    ]
)

def test_invalid_login(username, password, error_message, page):
    login_page = LoginPage(page)
    login_page.login(username, password)
    login_error_message = page.locator("[data-test='error']").text_content()
    assert error_message in login_error_message