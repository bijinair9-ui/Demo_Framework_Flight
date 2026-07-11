from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select
from time import sleep


class LoginPage(BasePage):

    login_btn = ("xpath", "(//button[contains(text(),'Sign')])[1]")
    frame_google = ("xpath", "//iframe[@title='Sign in with Google Button']")
    google_login_btn = ("xpath", "(//span[contains(text(),'Google')])")
    # use_another_account = ("xpath", "//div[text()='Use another account']")
    email = ("id", "identifierId")
    next_btn = ("xpath", "//span[text()='Next']/ancestor::button")
    continue_btn = ("xpath", "//span[text()='Continue']")


    def click_login(self):
        self.click(self.login_btn)

    def switch_frame(self):
        frame = WebDriverWait(self.driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it(self.frame_google)
        )
        return frame

    def click_google_btn(self):
        self.click(self.google_login_btn)
        self.driver.switch_to.default_content()

    def switch_to_google_window(self):
        """Switch to the newly opened Google login window."""
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def enter_email(self, email):
        self.enter_text(self.email, email)
        sleep(3)

    def click_next_btn(self):
        self.click(self.next_btn)





