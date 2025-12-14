from selenium.webdriver.common.by import By
from page_object_models.base_page import BasePage
from page_locators.contact_page_locator import ContactPageLocator
class ContactPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_title(self):
        return self.get_element(ContactPageLocator.TITLE_CONTACT)
    
    def type_name(self, name):
        self.type(ContactPageLocator.NAME_INPUT, name)

    def type_email(self, email):
        self.type(ContactPageLocator.EMAIL_INPUT, email)

    def type_phone(self, phone):
        self.type(ContactPageLocator.PHONE, phone)

    def type_message(self, message):
        self.type(ContactPageLocator.MESSAGE_TEXTAREA, message)

    def click_send(self):
        # use BasePage.click so we get the short wait
        self.click(ContactPageLocator.SEND_BUTTON)
    
    def is_contact_page_displayed(self):
        return self.get_title().is_displayed()
    
    def submit_contact_form(self, name, email, phone, message):
        self.type_name(name)
        self.type_email(email)
        self.type_phone(phone)
        self.type_message(message)
        self.click_send()

    def get_response_message(self):
        el = self.get_element(ContactPageLocator.RESPONSE_MESSAGE)
        return el.text