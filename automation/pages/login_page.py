from selenium.webdriver.common.by import By

from automation.pages.base_page import BasePage
from config.settings import BASE_URL


class LoginPage(BasePage):

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3")

    def open(self):
        super().open(BASE_URL)

    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def login_successful(self):
        return "inventory" in self.current_url()

    def error_message(self):
        try:
            return self.text(self.ERROR_MESSAGE)
        except Exception:
            return ""