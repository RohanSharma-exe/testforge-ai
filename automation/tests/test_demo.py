def test_framework(driver):

    driver.get("https://www.google.com")

    assert "Google" in driver.title