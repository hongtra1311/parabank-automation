from pages.login_page import LoginPage
import time
def test_invalid_login(login_page, driver):
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    time.sleep(2)  # Wait for page to load
    login_page.login("hongtra1311", "ztvz!96jFL3P@")
    time.sleep(3)  # Wait for page to load
    assert login_page.is_login_error()