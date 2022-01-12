import logging
import os

import allure
import pytest
from config import DefaultCreds
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    """
    Possibility of parameterization of the environment using different interface languages.
    To change the language, you must explicitly specify on the command line:
     <- language = en> or another language in standard abbreviation.
    """
    parser.addoption('--language',
                     action='store',
                     default='en',
                     help="Choose language: ru, en, fr, it, es ... (etc.)"
                     )
    parser.addoption('--user',
                     action='store',
                     default='None',
                     help="Set a username"
                     )
    parser.addoption('--password',
                     action='store',
                     default='None',
                     help="Set a password"
                     )


@pytest.fixture()
def user(request):
    user_cmd = request.config.getoption("user")
    if user_cmd == "None":
        return DefaultCreds.USERNAME
    else:
        return user_cmd


@pytest.fixture()
def password(request):
    password_cmd = request.config.getoption("password")
    if password_cmd == "None":
        return DefaultCreds.PASSWORD
    else:
        return password_cmd


@pytest.fixture(scope="session")
def browser(request):
    """
    Method automatically initializes driver for Chrome browser.
    """
    user_language = request.config.getoption("language")
    options = Options()
    options.add_argument("start-maximized")
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_language})
    
    browser = webdriver.Chrome(ChromeDriverManager(log_level=logging.ERROR).install(), options=options)
    yield browser
    browser.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'browser' in item.fixturenames:
                    web_driver = item.funcargs['browser']
                else:
                    print('Fail to take screen-shot')
                    return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))
