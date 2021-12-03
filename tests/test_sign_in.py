import allure
import pytest

from pages.guest_main_page import GuestMainPage
from pages.login_page import LoginPage
from pages.user_main_page import UserMainPage
from utils.links import Links


@allure.feature('Guest login actions on the main page')
@allure.severity(allure.severity_level.CRITICAL)
class TestSignInFromMainPage:
    @allure.story('Guest sees link to sign in')
    @pytest.mark.guest_actions
    def test_guest_should_see_login_link(self, browser):
        guest_main_page = GuestMainPage(browser, Links.MAIN_PAGE_LINK)
        guest_main_page.open()
        guest_main_page.should_be_login_link()

    @allure.story('Guest can click on the link to sign in')
    @pytest.mark.guest_actions
    def test_guest_can_go_to_login_page(self, browser):
        guest_main_page = GuestMainPage(browser, Links.MAIN_PAGE_LINK)
        guest_main_page.open()
        guest_main_page.go_to_login_page()
        guest_login_page = LoginPage(browser, browser.current_url)
        guest_login_page.should_be_login_page()

    @allure.story('Guest can click on the link and sign in. Test should verified it by actual name')
    @pytest.mark.guest_actions
    @pytest.mark.sign_in
    def test_guest_can_sign_in_test_user(self, browser):
        guest_main_page = GuestMainPage(browser, Links.MAIN_PAGE_LINK)
        guest_main_page.open()
        guest_main_page.go_to_login_page()
        guest_login_page = LoginPage(browser, browser.current_url)
        guest_login_page.sign_in_test_user()
        user_main_page = UserMainPage(browser, browser.current_url)
        user_main_page.should_be_correct_user()
