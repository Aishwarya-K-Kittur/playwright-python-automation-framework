class BasePage:

    def __init__(self, page):
        self.page = page

    def click(self, locator):
        locator.click()


    def fill(self, locator, text):
        locator.fill(text)

    def get_text(self, locator):
        return locator.text_content()

    def get_count(self, locator):
        return locator.count()