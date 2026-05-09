class CartPage:
    def __init__(self, page):
        self.page = page

    def get_cart_items_count(self):
        return self.page.locator(".cart_item").count()


    def remove_backpack(self):
        self.page.locator("#remove-sauce-labs-backpack").click()

    def click_checkout(self):
        self.page.locator("#checkout").click()