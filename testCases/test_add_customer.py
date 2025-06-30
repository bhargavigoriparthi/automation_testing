import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomerPage
import time

class Test_002_AddCustomer:
    baseURL = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"

    def test_addCustomer(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        lp = LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(2)

        addcust = AddCustomerPage(self.driver)
        addcust.clickOnCustomersMenu()
        time.sleep(1)
        addcust.clickOnCustomersMenuItem()


