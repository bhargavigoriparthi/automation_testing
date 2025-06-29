import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def setup():
    options = Options()
    options.add_argument("--start-maximized")
    serv_obj = Service("C:\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj, options=options)
    return driver
