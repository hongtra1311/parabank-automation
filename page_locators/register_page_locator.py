from selenium.webdriver.common.by import By
from page_locators.base_page_locator import BasePageLocator

class RegisterPageLocator(BasePageLocator):
    '''
    Register Page Locators
    '''
    REGISTER_LINK = (By.LINK_TEXT, "Register")
    TITLE_REGISTER = (By.XPATH, "//h1[text()='Signing up is easy!']")
    REGISTER_NAME = (By.ID, "customer.firstName")
    REGISTER_LAST_NAME = (By.ID, "customer.lastName")
    REGISTER_ADDRESS = (By.ID, "customer.address.street")
    REGISTER_CITY = (By.ID, "customer.address.city")
    REGISTER_STATE = (By.ID, "customer.address.state")
    REGISTER_ZIP_CODE = (By.ID, "customer.address.zipCode")
    REGISTER_PHONE = (By.ID, "customer.phoneNumber")
    REGISTER_SSN = (By.ID, "customer.ssn")
    REGISTER_USERNAME = (By.ID, "customer.username")
    REGISTER_PASSWORD = (By.ID, "customer.password")
    REGISTER_CONFIRM_PASSWORD = (By.ID, "repeatedPassword")
    REGISTER_BUTTON = (By.XPATH, "//input[@value='Register']")
    ACCOUNT_OVERVIEW = (By.XPATH, "//p[text()='Your account was created successfully. You are now logged in.']")