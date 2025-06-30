from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
import time

class LoginPage:
    textbox_username_xpath = "//input[@id='Email']"
    textbox_password_xpath = "//input[@id='Password']"
    button_login_xpath = "//button[@type='submit']"
    link_logout_xpath = "//a[contains(text(),'Logout')]"
    dashboard_header_xpath = "//h1[contains(text(),'Dashboard')]"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def setUserName(self, username):
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.textbox_username_xpath))).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)
        print("Entered username.")

    def setPassword(self, password):
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.textbox_password_xpath))).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)
        print("Entered password.")

    def clickLogin(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_login_xpath))).click()
        print("Clicked login button.")
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.dashboard_header_xpath)))
            print("Login successful. Dashboard loaded.")
        except TimeoutException:
            print("Login failed or dashboard not loaded in time.")
            self.driver.save_screenshot("Screenshots/login_failure.png")
            with open("page_source.html", "w", encoding="utf-8") as f:
                f.write(self.driver.page_source)
            raise

    def clickLogout(self):
        try:
            # Wait for modal or overlay to disappear
            self._wait_for_modal_to_disappear()
            # Try clicking logout
            logout_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.link_logout_xpath)))
            logout_btn.click()
            print("Clicked logout.")
        except ElementClickInterceptedException:
            print("Click intercepted. Retrying after 2 seconds...")
            time.sleep(2)
            self._wait_for_modal_to_disappear()
            self.driver.find_element(By.XPATH, self.link_logout_xpath).click()

    def _wait_for_modal_to_disappear(self):
        time.sleep(1)  # Initial wait for modal animation
        try:
            WebDriverWait(self.driver, 10).until_not(
                EC.presence_of_element_located((By.ID, "loadCustomerStatisticsAlert-action-alert"))
            )
            print("Modal popup disappeared.")
        except TimeoutException:
            print("Modal popup did not disappear. Continuing anyway.")
