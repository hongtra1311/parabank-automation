import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from page_object_models.login_page import LoginPage
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture
def register_page(driver):
    from page_object_models.register_page import RegisterPage
    return RegisterPage(driver)

@pytest.fixture
def about_page(driver):
    from page_object_models.about_page import AboutPage
    return AboutPage(driver)

@pytest.fixture
def contact_page(driver):
    from page_object_models.contact_page import ContactPage
    return ContactPage(driver)