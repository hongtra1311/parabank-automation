import pytest
from page_object_models.contact_page import ContactPage

@pytest.mark.order(4)
def test_display_contact_page(contact_page, driver):
    driver.get("https://parabank.parasoft.com/parabank/contact.htm")
    assert contact_page.is_contact_page_displayed()
    contact_page.submit_contact_form("John Doe", "john.doe@example.com", "1234567890", "Test message")
    contact_page.screenshot("contact_page_display")
    if contact_page.get_response_message():
        assert True
    else:
        assert False