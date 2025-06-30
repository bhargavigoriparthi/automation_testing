from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddCustomerPage:
    lnk_customers_menu_xpath = "//nav//p[contains(text(),'Customers')]"
    lnk_customers_menuitem_xpath = "//a[@href='/Admin/Customer/List']"
    header_customers_xpath = "//h1[contains(text(),'Customers')]"  # NEW

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def clickOnCustomersMenu(self):
        print("Clicking on Customers menu")
        menu = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.lnk_customers_menu_xpath)))
        menu.click()

    def clickOnCustomersMenuItem(self):
        print("Clicking on Customers submenu")
        submenu = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.lnk_customers_menuitem_xpath)))
        submenu.click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.header_customers_xpath)))  # NEW
