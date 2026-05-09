class CheckoutPage:
    def __init__(self, page):
        self.page = page

    def fill_checkout_information(self):
        self.page.locator("#first-name").fill("Aishwarya")
        self.page.locator("#last-name").fill("K K")
        self.page.locator("#postal-code").fill("580112")

    def click_continue(self):
        self.page.locator("#continue").click()

    def click_finish(self):
        self.page.locator("#finish").click()

    def get_order_success_message(self):
        return self.page.locator(".complete-header").text_content()
