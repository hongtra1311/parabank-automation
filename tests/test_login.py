import pytest
from page_object_models.login_page import LoginPage


@pytest.mark.order(2)
def test_invalid_login(login_page, driver):
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    login_page.login("hongtra1311", "ztvz!96jFL3P@")
    if login_page.get_error_message():
        assert True
    else:
        assert False