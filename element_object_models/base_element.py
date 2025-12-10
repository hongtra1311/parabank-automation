import selenium.webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, \
TimeoutException, \
NoSuchAttributeException

class BaseElement: 
    """
    Base Web Element 
    """

    def __init__(self, driver: selenium.webdriver, explicit_wait: int, locator: None):
        self._driver = self._set_driver(driver)
        self._explicit_wait = explicit_wait
        self._locator = self._set_locator(locator)
        self._element = self._set_element()

    @property
    def explicit_wait(self):
        """
        Return Explicit wait value
        """
        return self._explicit_wait
    
    @property
    def driver(self):
        """
        Return WebDriver instance
        """
        return self._driver
    
    def attribute(self, attribute_name: str):
        """
        Return attribute value of the element
        """
        try:
            return self._element.get_attribute(attribute_name)
        except TimeoutException:
            raise NoSuchAttributeException(
                '\nERROR: The element has no attribute "{}".\n'
                'LOCATOR: {}\n'.format(attribute_name, self.locator))
        

    @property
    def locator(self):
        """
        Return locator of the element
        """
        return self._locator
    
    @property
    def element(self):
        """
        Return WebElement instance
        """
        return self._element
    
    def _find_element(self):
        """
        Find element with explicit wait
        """
        try:
            wait = WebDriverWait(self.driver, self.explicit_wait)
            element = wait.until(EC.presence_of_element_located(self.locator))
            return element
        except TimeoutException:
            raise NoSuchElementException(
                '\nERROR: The element could not be found on the page within {} seconds.\n'
                'LOCATOR: {}\n'.format(self.explicit_wait, self.locator))
    
    @staticmethod
    def _set_driver(self, driver: selenium.webdriver):
        """
        Set WebDriver instance
        """
        return driver
    
    @staticmethod
    def _check_driver_type(driver: selenium.webdriver):
        """
        Debug only
        """
        if driver.DesiredCapabilities['browserName'] == 'chrome':
            if not isinstance(driver, selenium.webdriver.Chrome):
                raise TypeError(
                    '\nERROR: The driver is not a Chrome WebDriver instance.\n'
                    'Actual type: {}\n'.format(type(driver)))
            return None
        
        if driver.DesiredCapabilities['browserName'] == 'firefox':
            if not isinstance(driver, selenium.webdriver.Firefox):
                raise TypeError(
                    '\nERROR: The driver is not a Firefox WebDriver instance.\n'
                    'Actual type: {}\n'.format(type(driver)))
            return None
        
        if driver.DesiredCapabilities['browserName'] == 'MicrosoftEdge':
            if not isinstance(driver, selenium.webdriver.Edge):
                raise TypeError(
                    '\nERROR: The driver is not a Edge WebDriver instance.\n'
                    'Actual type: {}\n'.format(type(driver)))
            return None
        
        raise TypeError(
            '\nERROR: Unsupported WebDriver instance.\n'
            'Actual type: {}\n'.format(type(driver)))
    
    @staticmethod
    def _set_locator(locator: tuple):
        """
        Set locator
        """
        if not isinstance(locator, tuple):
            raise TypeError(
                '\nERROR: The locator is not a tuple.\n'
                'Actual type: {}\n'.format(type(locator)))
        return locator