from page_object_models.login_page import LoginPage
import time
def test_invalid_login(login_page, driver):
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    login_page.login("hongtra1311", "ztvz!96jFL3P@")
    time.sleep(1)  
    assert login_page.is_login_error()