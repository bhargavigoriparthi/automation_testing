from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchCustomerPage:
    txt_email_xpath = "//input[@id='SearchEmail']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def setEmail(self, email):
        print("Entering email to search")
        email_field = self.wait.until(EC.presence_of_element_located((By.XPATH, self.txt_email_xpath)))
        email_field.clear()
        email_field.send_keys(email)
