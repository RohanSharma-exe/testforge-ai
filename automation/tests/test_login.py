import pytest

from automation.pages.login_page import LoginPage
from test_data.login_data import LOGIN_DATA


@pytest.mark.parametrize(
    "username,password,expected",
    LOGIN_DATA
)
def test_login(driver, username, password, expected):

    page = LoginPage(driver)

    page.open()

    page.login(username, password)

    assert page.login_successful() == expected