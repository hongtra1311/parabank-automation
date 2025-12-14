from selenium.webdriver.common.by import By
from page_locators.base_page_locator import BasePageLocator

class HomePageLocator(BasePageLocator):
    '''
    Home Page Locators
    '''
    INTRODUCE_HOME = (By.XPATH, "//p[text()='Experience the difference']")

    # Left menu
    ABOUT_US = (By.CSS_SELECTOR, "ul.leftmenu > li:nth-child(1)")

    # Header links
    HOME_LINK = (By.XPATH, "//div[@id='headerPanel']//li[@class='home']/a")
    ABOUT_LINK = (By.XPATH, "//div[@id='headerPanel']//li[@class='aboutus']/a")
    CONTACT_LINK = (By.XPATH, "//div[@id='headerPanel']//li[@class='contact']/a")

