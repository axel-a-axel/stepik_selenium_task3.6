import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser = None
    if language == None:
        raise pytest.UsageError("--language should be defined - en, ru, etc.")
    else:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
        yield browser
        print("\nquit browser..")
        browser.quit()