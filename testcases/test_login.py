from time import sleep
from selenium import webdriver
driver = webdriver
import pytest

from pages.login_page import LoginPage
from utilities import read_excel

@pytest.mark.parametrize("username,password", read_excel.get_data())


def test_login(setup_and_teardown, username, password):
    lp = LoginPage(setup_and_teardown)
    lp.click_login()
    lp.switch_frame()
    lp.click_google_btn()
    lp.switch_to_google_window()
    lp.enter_email(username)
    lp.take_screenshot()








