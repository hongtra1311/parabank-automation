from selenium.webdriver.common.by import By
from page_object_models.base_page import BasePage
from page_locators.login_page_locator import LoginPageLocator

class LoginPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.get_element(LoginPageLocator.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password):
        self.get_element(LoginPageLocator.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        self.get_element(LoginPageLocator.LOGIN_BUTTON).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        return self.get_element(LoginPageLocator.ACCOUNT_OVERVIEW)