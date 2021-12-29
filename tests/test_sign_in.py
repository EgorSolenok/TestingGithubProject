import allure
import pytest

from config import IdentityUrl
from tests.assertions.assertions import Assertions
from tests.pages.locators.locators import BasePageLocators
from tests.pages.locators.locators import HeaderUserPageLocators
from tests.pages.locators.locators import LoginPageLocators
from tests.pages.user_main_page import UserMainPage


@allure.feature('Guest login actions on the main page')
@allure.severity(allure.severity_level.CRITICAL)
class TestSignInFromMainPage:
    @allure.story('Guest sees link to sign in')
    @pytest.mark.guest_actions
    def test_guest_should_see_login_link(self, browser, guest_main_page):
        guest_main_page.open()
        Assertions.should_be_element(browser, *BasePageLocators.LOGIN_LINK)

    @allure.story('Guest can click on the link to sign in')
    @pytest.mark.guest_actions
    def test_guest_can_go_to_login_page(self, browser, guest_main_page):
        guest_main_page.open()
        guest_main_page.go_to_login_page()
        Assertions.should_be_element(browser, *LoginPageLocators.USERNAME_FORM)
        Assertions.should_be_element(browser, *LoginPageLocators.PASSWORD_FORM)
        Assertions.should_be_correct_url(browser, IdentityUrl.LoginPage)

    @allure.story('Guest can click on the link and sign in. Test should verified it by actual name')
    @pytest.mark.guest_actions
    @pytest.mark.sign_in
    def test_guest_can_sign_in_test_user(self, browser, guest_main_page, login_page, user, password):
        guest_main_page.open()
        guest_main_page.go_to_login_page()
        login_page.sign_in_test_user(user, password)
        user_main_page = UserMainPage(browser, browser.current_url)
        user_main_page.go_to_dropdown_profile_list()
        Assertions.should_be_element(browser, *HeaderUserPageLocators.USER_ICON)
        Assertions.phrase_should_contain_text(browser, *HeaderUserPageLocators.USER_NAME_IN_PROFILE_MENU, phrase=user)
