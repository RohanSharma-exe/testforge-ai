import pytest

from utils.driver import get_driver
from utils.logger import log


@pytest.fixture()
def driver():

    driver = get_driver()

    yield driver

    log.info("Closing browser")

    driver.quit()