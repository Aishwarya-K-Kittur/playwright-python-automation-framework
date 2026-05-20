from pages.base_page import BasePage
class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.add_to_cart_sause_labs_backback = page.locator("#add-to-cart-sauce-labs-backpack")
        self.add_to_cart_sause_labs_bike_light = page.locator("#add-to-cart-sauce-labs-bike-light")
        self.shopping_cart_link = page.locator(".shopping_cart_link")

    def add_backpack_to_cart(self):
        self.click(self.add_to_cart_sause_labs_backback)

    def add_bike_light_to_cart(self):
        self.click(self.add_to_cart_sause_labs_bike_light)

    def go_to_cart(self):
        self.click(self.shopping_cart_link)