from selenium.webdriver.common.by import By
from page_locators.base_page_locator import BasePageLocator

class LoginPageLocator(BasePageLocator):
    '''
    Login Page Locators
    '''
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='Log In']")
    ACCOUNT_OVERVIEW = (By.XPATH, "//p[@class='error' and text()='The username and password could not be verified.']")