import pytest
from datetime import datetime

from utils.driver import get_driver
from config.settings import SCREENSHOT_DIR
from utils.logger import log


@pytest.fixture()
def driver():
    driver = get_driver()
    yield driver
    log.info("Closing browser")
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:

            filename = datetime.now().strftime("%Y%m%d_%H%M%S")

            path = SCREENSHOT_DIR / f"{filename}.png"

            driver.save_screenshot(str(path))

            log.error(f"Screenshot saved -> {path}")