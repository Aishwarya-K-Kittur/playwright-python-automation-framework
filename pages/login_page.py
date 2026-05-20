from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")

    def login(self, username, password):
        print("Login method")
        self.fill(self.username_input, username)
        self.fill(self.password_input, password)
        self.click(self.login_button)


