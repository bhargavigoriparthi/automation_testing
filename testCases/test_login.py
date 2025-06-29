import time
import pytest
from pageObjects.loginPage import LoginPage

def test_login(setup):
    driver = setup
    driver.get("https://admin-demo.nopcommerce.com/login")  # ✅ Correct URL

    login_page = LoginPage(driver)
    login_page.setUsername("admin@yourstore.com")
    login_page.setPassword("admin")
    login_page.clickLogin()

    time.sleep(3)  # Wait for the dashboard to load
    assert "dashboard" in driver.page_source.lower()  # ✅ More reliable than title
