import pytest
from page_object_models.about_page import AboutPage


@pytest.mark.order(1)
def test_display_about_page(about_page, driver):
    driver.get("https://parabank.parasoft.com/parabank/about.htm")
    # about_page.login("hongtra1311", "ztvz!96jFL3P@")
    assert about_page.is_about_page_displayed()
    about_page.screenshot("about_page_display")