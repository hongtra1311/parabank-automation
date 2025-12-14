from time import time
from selenium.webdriver.common.by import By
import time
from page_object_models.base_page import BasePage
from page_locators.register_page_locator import RegisterPageLocator
class RegisterPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    def click_register_link(self):
        self.get_element(RegisterPageLocator.REGISTER_LINK).click()

    def enter_name(self, name):
        self.get_element(RegisterPageLocator.REGISTER_NAME).send_keys(name)

    def enter_last_name(self, last_name):
        self.get_element(RegisterPageLocator.REGISTER_LAST_NAME).send_keys(last_name)

    def enter_address(self, address):
        self.get_element(RegisterPageLocator.REGISTER_ADDRESS).send_keys(address)

    def enter_city(self, city):
        self.get_element(RegisterPageLocator.REGISTER_CITY).send_keys(city)

    def enter_state(self, state):
        self.get_element(RegisterPageLocator.REGISTER_STATE).send_keys(state)

    def enter_zip_code(self, zip_code):
        self.get_element(RegisterPageLocator.REGISTER_ZIP_CODE).send_keys(zip_code)

    def enter_phone(self, phone):
        self.get_element(RegisterPageLocator.REGISTER_PHONE).send_keys(phone)

    def enter_ssn(self, ssn):
        self.get_element(RegisterPageLocator.REGISTER_SSN).send_keys(ssn)

    def enter_username(self, username):
        self.get_element(RegisterPageLocator.REGISTER_USERNAME).send_keys(username)

    def enter_password(self, password):
        self.get_element(RegisterPageLocator.REGISTER_PASSWORD).send_keys(password)

    def enter_confirm_password(self, confirm_password):
        self.get_element(RegisterPageLocator.REGISTER_CONFIRM_PASSWORD).send_keys(confirm_password)

    def click_register(self):
        self.get_element(RegisterPageLocator.REGISTER_BUTTON).click()

    def register(self):
        self.click_register_link()
        self.get_element(RegisterPageLocator.TITLE_REGISTER)
        self.enter_name("John")
        self.enter_last_name("Doe")
        self.enter_address("123 Main St")
        self.enter_city("Anytown")
        self.enter_state("Anystate")
        self.enter_zip_code("12345")
        self.enter_phone("555-1234")
        self.enter_ssn("123-45-6789")
        self.enter_username("johndoe" + str(int(time.time())))
        self.enter_password("password123")
        self.enter_confirm_password("password123")
        self.click_register()

    def is_valid_register(self):
        return self.get_element(self.ACCOUNT_OVERVIEW)