from page_object_models.register_page import RegisterPage
def test_invalid_login(register_page, driver):
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    register_page.register()
    if register_page.is_valid_register():
        assert True
    else:
        assert False