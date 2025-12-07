from logging import log
from time import time
from selenium.webdriver.common.by import By
import time
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='Log In']")
    ACCOUNT_OVERVIEW = (By.XPATH, "//p[@class='error' and text()='The username and password could not be verified.']")

    def login(self, username, password):
        print(f"Logging in with username")
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        time.sleep(2)  
        self.click(self.LOGIN_BUTTON)

    def is_login_error(self):
        try:
            self.get_element(self.ACCOUNT_OVERVIEW)
            return True
        except:
            return False