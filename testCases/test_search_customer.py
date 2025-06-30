import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomerPage
from pageObjects.SearchCustomerPage import SearchCustomerPage

class Test_003_SearchCustomer:
    baseURL = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"

    def test_searchCustomer(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        lp = LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()

        time.sleep(2)  # wait for dashboard

        addcust = AddCustomerPage(self.driver)
        addcust.clickOnCustomersMenu()
        addcust.clickOnCustomersMenuItem()

        time.sleep(2)  # wait for customer page to load

        sc = SearchCustomerPage(self.driver)
        sc.setEmail("admin@yourstore.com")

        time.sleep(2)  # optional pause for visual confirmation
