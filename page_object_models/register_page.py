from time import time
from selenium.webdriver.common.by import By
import time
from page_object_models.base_page import BasePage

class RegisterPage(BasePage):
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

    def register(self):
        print(f"Registering a new user")
        self.click(self.REGISTER_LINK)
        self.get_element(self.TITLE_REGISTER)
        self.type(self.REGISTER_NAME, "John")
        self.type(self.REGISTER_LAST_NAME, "Doe")
        self.type(self.REGISTER_ADDRESS, "123 Main St")
        self.type(self.REGISTER_CITY, "Anytown")    
        self.type(self.REGISTER_STATE, "CA")
        self.type(self.REGISTER_ZIP_CODE, "12345")
        self.type(self.REGISTER_PHONE, "555-1234")
        self.type(self.REGISTER_SSN, "123-45-6789")
        self.type(self.REGISTER_USERNAME, "johndoe"+ str(int(time.time())))
        self.type(self.REGISTER_PASSWORD, "password123")
        self.type(self.REGISTER_CONFIRM_PASSWORD, "password123")
        time.sleep(2)
        self.click(self.REGISTER_BUTTON)
        time.sleep(2)

    def is_valid_register(self):
        try:
            self.get_element(self.ACCOUNT_OVERVIEW)
            return True
        except:
            return False