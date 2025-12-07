import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
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