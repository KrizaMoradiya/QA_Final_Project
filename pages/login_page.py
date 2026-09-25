from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.login_button = page.locator("#login-button")

    def open(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()