import logging

import pytest
import allure
import time
from datetime import datetime
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



@pytest.fixture(scope="session")
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

    # if request.node.rep_call.failed:
    #     # Make the screen-shot if test failed:
    #     try:
    #         browser.execute_script("document.body.bgColor = 'white';")
    #
    #         allure.attach(browser.get_screenshot_as_png(),
    #                       name=request.function.__name__,
    #                       attachment_type=allure.attachment_type.PNG)
    #     except:
    #         browser.execute_script("document.body.bgColor = 'white';")
    #
    #         allure.attach(browser.get_screenshot_as_png(),
    #                       name=request.function.__name__,
    #                       attachment_type=allure.attachment_type.PNG)
    browser.quit()

# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()
#     setattr(item, "rep_" + rep.when, rep)
#     return rep






