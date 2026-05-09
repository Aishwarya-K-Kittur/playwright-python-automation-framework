from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_checkout_flow(page):
    login_page = LoginPage(page)
    login_page.login("standard_user","secret_sauce")

    inventory_page = InventoryPage(page)

    inventory_page.add_backpack_to_cart()
    inventory_page.add_bike_light_to_cart()
    inventory_page.go_to_cart()

    cart_page = CartPage(page)
    cart_page.click_checkout()

    checkout_age = CheckoutPage(page)
    checkout_age.fill_checkout_information()
    checkout_age.click_continue()
    checkout_age.click_finish()
    success_message = checkout_age.get_order_success_message()

    assert success_message == "Thank you for your order!"