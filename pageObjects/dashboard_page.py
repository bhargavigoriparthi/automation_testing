import time
from selenium.webdriver.common.by import By

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.welcome_menu = (By.ID, "welcome")
        self.logout_link = (By.LINK_TEXT, "Logout")

    def clickLogout(self):
        self.driver.find_element(*self.welcome_menu).click()
        time.sleep(2)
        self.driver.find_element(*self.logout_link).click()
