import pytest

from config import DefaultUrl
from tests.pages.guest_main_page import GuestMainPage
from tests.pages.login_page import LoginPage


@pytest.fixture(scope='package')
def guest_main_page(browser):
    guest_main_page = GuestMainPage(browser, DefaultUrl.MAIN_URL)
    yield guest_main_page
    
@pytest.fixture(scope='package')
def login_page(browser):
    login_page = LoginPage(browser, DefaultUrl.LOGIN_URL)
    yield login_page
