from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from playwright.sync_api import expect
import pytest

@pytest.mark.sanity
def test_checkout_flow(page):
    login_page = LoginPage(page)
    login_page.login("standard_user","secret_sauce")

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator(".title")).to_have_text("Products")

    inventory_page = InventoryPage(page)

    inventory_page.add_backpack_to_cart()
    inventory_page.add_bike_light_to_cart()
    expect(page.locator(".shopping_cart_badge")).to_have_text("2")

    inventory_page.go_to_cart()
    expect(page.locator(".title")).to_have_text("Your Cart")

    cart_page = CartPage(page)
    expect(page.locator(".cart_item")).to_have_count(2)
    cart_page.click_checkout()

    checkout_age = CheckoutPage(page)
    expect(page.locator(".title")).to_have_text("Checkout: Your Information")
    checkout_age.fill_checkout_information()

    checkout_age.click_continue()
    expect(page.locator(".title")).to_have_text("Checkout: Overview")

    checkout_age.click_finish()
    success_message = checkout_age.get_order_success_message()
    expect(page.locator(".complete-header")).to_have_text("Thank you for your order!")

@pytest.mark.regression
def test_title(page):
    #negative scenario - if below line is added then tc will fail
    assert "wrong" in page.url
    assert "Swag Labs" in page.title()
    print("validation of swag labs in page title is completed")

def test_url(page):
    assert "saucedemo" in page.url
    print("validation of saucedemo in page url is completed")

def test_inventory_page(logged_in_page):
    assert "inventory" in logged_in_page.url

def test_inventory_page(logged_in_page):

    assert "inventory" in logged_in_page.url

def test_login_validation(logged_in_page):
    expect(logged_in_page).to_have_url("https://www.saucedemo.com/inventory.html")

    expect(logged_in_page.locator(".title")).to_have_text("Products")