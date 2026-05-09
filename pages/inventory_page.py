class InventoryPage:
    def __init__(self, page):
        self.page = page

    def add_backpack_to_cart(self):
        self.page.locator("#add-to-cart-sauce-labs-backpack").click()

    def add_bike_light_to_cart(self):
        self.page.locator("#add-to-cart-sauce-labs-bike-light").click()

    def go_to_cart(self):
        self.page.locator(".shopping_cart_link").click()

