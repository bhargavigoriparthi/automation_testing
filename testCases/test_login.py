import pytest
from pageObjects.LoginPage import LoginPage

class Test_001_Login:
    baseURL = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"

    @pytest.mark.sanity
    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        lp = LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()

        actual_title = self.driver.title
        expected_title = "Dashboard / nopCommerce administration"

        assert actual_title == expected_title, f"Expected title '{expected_title}' but got '{actual_title}'"

        lp.clickLogout()
        self.driver.quit()
