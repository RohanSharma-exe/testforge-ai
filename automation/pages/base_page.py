from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.settings import TIMEOUT
from utils.logger import log


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, TIMEOUT)

    def open(self, url):
        log.info(f"Opening {url}")
        self.driver.get(url)

    def click(self, locator):
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    def type(self, locator, text):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    def text(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).text

    def visible(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def current_url(self):
        return self.driver.current_url