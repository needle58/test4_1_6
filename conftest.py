import time
from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as OptionsFF


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en')
    parser.addoption('--browser_name', action='store', default='chrome', help="Choose browser: chrome or firefox")
@pytest.fixture(scope="function")
def browser(request):

    browser_name = request.config.getoption("browser_name")
    browser_lang = request.config.getoption('language')
    #for chrome
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_lang})
    #for ff
    options_ff = OptionsFF()
    options_ff.set_preference("intl.accept_languages", browser_lang)
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(options=options_ff)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
