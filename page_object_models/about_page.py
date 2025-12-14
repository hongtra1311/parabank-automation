from selenium.webdriver.common.by import By
from page_object_models.base_page import BasePage
from page_locators.about_page_locator import AboutPageLocator

class AboutPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.get_element(AboutPageLocator.TITLE_ABOUT)

    def get_version_info(self):
        return self.get_element(AboutPageLocator.VERSION_INFO)

    def get_more_info_link(self):
        return self.get_element(AboutPageLocator.MORE_INFO_LINK)
    
    def is_about_page_displayed(self):
        return self.get_title().is_displayed() and \
               self.get_version_info().is_displayed() and \
               self.get_more_info_link().is_displayed()