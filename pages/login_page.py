class LoginPage:
    def __init__(self, page):
        self.page = page
    def login(self, username, password):
        print("Login method")
        self.page.fill("#user-name",username)
        self.page.fill("#password",password)
        self.page.locator("#login-button").click()

