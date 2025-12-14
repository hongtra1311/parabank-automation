import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from page_object_models.login_page import LoginPage
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.add_argument(
        "--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )

    options.add_experimental_option(
        "excludeSwitches", ["enable-automation"]
    )
    options.add_experimental_option(
        "useAutomationExtension", False
    )

    options.add_argument("--user-data-dir=./chrome-profile")
    options.add_argument("--profile-directory=Default")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.execute_cdp_cmd(
        "Page.addScriptToEvaluateOnNewDocument",
        {
            "source": """
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            });
            """
        }
    )
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

@pytest.fixture
def home_page(driver):
    from page_object_models.home_page import HomePage
    return HomePage(driver)