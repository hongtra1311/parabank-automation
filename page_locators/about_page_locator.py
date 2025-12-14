from selenium.webdriver.common.by import By
from page_locators.base_page_locator import BasePageLocator

class AboutPageLocator(BasePageLocator):
    '''
    About Page Locators
    '''
    TITLE_ABOUT = (By.XPATH, "//h1[text()='ParaSoft Demo Website']")
    VERSION_INFO = (By.XPATH, "//p[contains(text(),'ParaBank is a demo site used for demonstration of Parasoft software solutions.')]")
    MORE_INFO_LINK = (By.LINK_TEXT, "www.parasoft.com")