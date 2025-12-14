from selenium.webdriver.common.by import By
from page_object_models.base_page import BasePage
from page_locators.home_page_locator import HomePageLocator
class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_introduce_home(self):
        return self.get_element(HomePageLocator.INTRODUCE_HOME)
    
    def get_about_us_link(self):
        return self.get_element(HomePageLocator.ABOUT_US)
    
    def get_home_link(self):
        return self.get_element(HomePageLocator.HOME_LINK)
    
    def get_about_link(self):
        return self.get_element(HomePageLocator.ABOUT_LINK)
    
    def get_contact_link(self):
        return self.get_element(HomePageLocator.CONTACT_LINK)
    
    def display_home_page(self):
        return self.get_introduce_home().is_displayed() and \
               self.get_home_link().is_displayed() and \
               self.get_about_link().is_displayed() and \
               self.get_contact_link().is_displayed() and \
               self.get_about_us_link().is_displayed()