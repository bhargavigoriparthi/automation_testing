# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
#
# @pytest.fixture()
# def setup():
#     service = Service("C:/chromedriver-win64/chromedriver.exe")  # ✅ Your path
#     driver = webdriver.Chrome(service=service)
#     driver.maximize_window()
#     return driver
import pytest
from selenium import webdriver

@pytest.fixture()
def setup():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()