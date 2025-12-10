from element_object_models.base_element import BaseElement
from selenium.webdriver.support.wait  import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoSuchAttributeException

class Element(BaseElement):

    @property
    def element_src(self):
        """
        Return 'src' attribute of the element
        """
        return self.attribute("src")
    
    @property
    def element_class(self):
        """
        Return 'class' attribute of the element
        """
        return self.attribute("class")
    
    @property
    def element_alt(self):
        """
        Return 'alt' attribute of the element
        """
        return self.attribute("alt")
    
    @property
    def element_title(self):
        """
        Return 'title' attribute of the element
        """
        return self.attribute("title")
    
    @property
    def element_href(self):
        """
        Return 'href' attribute of the element
        """
        return self.attribute("href")
    
    @property
    def element_type(self):
        """
        Return 'type' attribute of the element
        """
        return self.attribute("type")
    
    @property
    def element_value(self):
        """
        Return 'value' attribute of the element
        """
        return self.attribute("value")
    
    @property
    def element_name(self):
        """
        Return 'name' attribute of the element
        """
        return self.attribute("name")
    
    @property
    def element_target(self):
        """
        Return 'target' attribute of the element
        """
        return self.attribute("target")
    
    @property
    def text(self):
        """
        Return text of the element
        """
        try:
            return self._element.text
        except TimeoutException:
            raise NoSuchElementException(
                '\nERROR: The element text could not be retrieved within {} seconds.\n'
                'LOCATOR: {}\n'.format(self.explicit_wait, self.locator))
        

    def click_on(self):
        """
        Click on the element
        """
        try:
            wait = WebDriverWait(self.driver, self.explicit_wait)
            element = wait.until(EC.element_to_be_clickable(self.locator))
            element.click()

        except TimeoutException:
            raise NoSuchElementException(
                '\nERROR: The element could not be clicked within {} seconds.\n'
                'LOCATOR: {}\n'.format(self.explicit_wait, self.locator))
        
    def is_visable(self):
        """
        Return True if the element is visible, else False
        """
        try:
            wait = WebDriverWait(self.driver, self.explicit_wait)
            visible = wait.until(EC.visibility_of_element_located(self.locator))
            return True
        except TimeoutException:
            return False
        
    def write(self, text: str):
        """
        Write text into the element
        """
        try:
            element = self._find_element()
            element.send_keys(text)
        except TimeoutException:
            raise NoSuchElementException(
                '\nERROR: The element could not be written into within {} seconds.\n'
                'LOCATOR: {}\n'.format(self.explicit_wait, self.locator))