from selenium.webdriver.common.by import By
from page_locators.base_page_locator import BasePageLocator

class ContactPageLocator(BasePageLocator):
    '''
    Contact Page Locators
    '''
    TITLE_CONTACT = (By.XPATH, "//h1[text()='Customer Care']")
    NAME_INPUT= (By.NAME, "name")
    EMAIL_INPUT = (By.NAME, "email")
    PHONE = (By.NAME, "phone")
    MESSAGE_TEXTAREA = (By.NAME, "message")
    SEND_BUTTON = (By.XPATH, "//input[@value='Send to Customer Care']")

    RESPONSE_MESSAGE = (By.XPATH, "//p[contains(text(),'Customer Care Representative will be contacting you.')]")