import pytest
import random
import string
from selenium import webdriver


@pytest.fixture()
def setUp(browser):
    global driver
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("***** Launching chrome browser ******")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("***** Launching Firefox browser ******")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


##########pytest-html report ###########

# It is hook for adding environment info to hml report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nopecommerceApp'
    config._metadata['Module Name'] = 'Signup'
    config._metadata['Tester'] = 'Prabhakar'


# It is hook for delete/modify Environment info to the HTML Report
def pytest_metadata(metadata):
    metadata.pop("Python Home", None)
    metadata.pop("Plugins", None)


def random_generator(size=8, chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
