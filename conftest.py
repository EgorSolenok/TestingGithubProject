import logging

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    '''
    Possibility of parameterization of the environment using different interface languages.
    To change the language, you must explicitly specify on the command line:
     <- language = en> or another language in standard abbreviation.
    '''
    parser.addoption('--language',
                     action='store', 
                     default='en',
                     help="Choose language: ru, en, fr, it, es ... (etc.)"
                    )



@pytest.fixture(scope="class")
def browser(request):
    '''
    Method automatically initializes driver for Chrome browser.
    '''
    user_language = request.config.getoption("language")
    options = Options()
    options.add_argument("start-maximized")
    options.add_experimental_option(
        'prefs',{'intl.accept_languages': user_language})

    browser = webdriver.Chrome(ChromeDriverManager(log_level=logging.ERROR).install(), options=options)
    yield browser
    browser.quit()


