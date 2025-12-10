from page_object_models.register_page import RegisterPage
import time
def test_invalid_login(register_page, driver):
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    register_page.register()
    time.sleep(1)  
    assert register_page.is_valid_register()