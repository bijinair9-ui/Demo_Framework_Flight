import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(params=["chrome",'firefox'])

def setup_and_teardown(request):

    parameter = request.param
    if parameter == "chrome":
        driver = webdriver.Chrome()
    if parameter == "firefox":
        driver = webdriver.FireFox()
        
    driver.implicitly_wait(10)
    driver.get("https://www.ixigo.com/")   #launch ixigo app
    driver.maximize_window()
    sleep(5)
    yield driver
    driver.quit()
