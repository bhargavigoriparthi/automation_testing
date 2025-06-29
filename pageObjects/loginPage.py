from selenium.webdriver.common.by import By

class LoginPage:
    txt_email_name = "Email"
    txt_password_name = "Password"
    btn_login_xpath = "//button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element(By.NAME, self.txt_email_name).clear()
        self.driver.find_element(By.NAME, self.txt_email_name).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.NAME, self.txt_password_name).clear()
        self.driver.find_element(By.NAME, self.txt_password_name).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()
