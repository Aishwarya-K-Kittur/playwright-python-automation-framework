from pages.base_page import BasePage
class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.cart_item = page.locator(".cart_item")
        self.btn_remove_sauce_labs_backpack = page.locator("#remove-sauce-labs-backpack")
        self.btn_checkout = page.locator("#checkout")

    def get_cart_items_count(self):
        return self.get_count(self.cart_item)

    def remove_backpack(self):
        self.click(self.btn_remove_sauce_labs_backpack)

    def click_checkout(self):
        self.click(self.btn_checkout)