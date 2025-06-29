import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def setup():
    serv_obj = Service("C:/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj)
    driver.maximize_window()
    yield driver
    driver.quit()
