import pytest
from page_object_models.home_page import HomePage


@pytest.mark.order(5)
def test_display_home_page(home_page, driver):
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    assert home_page.display_home_page()