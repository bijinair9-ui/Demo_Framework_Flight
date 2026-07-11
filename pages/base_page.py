from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import os
from datetime import datetime

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self, locator,text):
        self.wait.until(EC.visibility_of_element_located(locator)).clear()
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def select_visible_text(self, locator, text):
        Select(self.driver.find_element(*locator)).select_by_visible_text(text)

    def select_value(self, locator, value):
        Select(self.driver.find_element(*locator)).select_by_value(value)

    def take_screenshot(self, name=None):
        folder = os.path.join(os.getcwd(), "Screenshots")
        os.makedirs(folder, exist_ok=True)

        # If no name is provided, use timestamp
        if name is None:
            name = datetime.now().strftime("%Y%m%d%H%M%S") + ".png"

        path = os.path.join(folder, name)
        self.driver.save_screenshot(path)
        print(f"Screenshot saved at: {path}")
