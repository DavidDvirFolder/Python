from selenium import webdriver
import pytest


# Fixture to configure and return the browser instance
@pytest.fixture
def browser(request):
    browser_type = request.config.getoption("--browser")

    if browser_type == 'chrome':
        driver = webdriver.Chrome()
    elif browser_type == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()

    yield driver  # Provide the browser instance to tests
    driver.quit()


# Fixture to configure and return the setup
@pytest.fixture
def setup(browser):
    browser.maximize_window()
    return browser


# Pytest command-line option to specify the browser type
def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="Specify the browser: chrome or firefox")


# Pytest HTML Report
def pytest_configure(config):
    if hasattr(config, '_metadata'):
        config.metadata['Project Name'] = 'LUMA'
        config.metadata['Module Name'] = 'Customers'
        config.metadata['Tester'] = 'David'


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
