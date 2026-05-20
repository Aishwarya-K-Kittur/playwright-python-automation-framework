from pages.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        
        self.first_name = page.locator("#first-name")
        self.last_name = page.locator("#last-name")
        self.postal_code = page.locator("#postal-code")
        self.btn_continue = page.locator("#continue")
        self.btn_finish = page.locator("#finish")
        self.complete_header = page.locator(".complete-header")

    def fill_checkout_information(self):

        self.fill(self.first_name, "Aishwarya")
        self.fill(self.last_name, "K K")
        self.fill(self.postal_code, "580112")

    def click_continue(self):
        self.click(self.btn_continue)

    def click_finish(self):
        self.click(self.btn_finish)

    def get_order_success_message(self):
        return self.get_text(self.complete_header)
