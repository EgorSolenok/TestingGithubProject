import allure

from .base_page import BasePage
from tests.pages.locators.locators import LoginPageLocators
from utils.browser_helper import BrowserHelper


class LoginPage(BasePage):
    @allure.step("Verification of login page (correct URL, username and password forms")
    def should_be_login_page(self):
        """
        Complex verification for compliance with the login page. Method is using current URL, verification of
        username and passwords form on page.
        """
        self.should_be_login_url()
        self.should_be_username_form()
        self.should_be_password_form()

    @allure.step("Verification of correct URL of login page")
    def should_be_login_url(self):
        assert "github.com/login" in self.browser.current_url, "This page is not login page"

    @allure.step("Verification of username form")
    def should_be_username_form(self):
        assert BrowserHelper.find_visible_element(self.browser, *LoginPageLocators.USERNAME_FORM), "Username form is not presented"

    @allure.step("Verification of password form")
    def should_be_password_form(self):
        assert BrowserHelper.find_visible_element(self.browser, *LoginPageLocators.PASSWORD_FORM), "Password form is not presented"

    @allure.step(f"Signing in")
    def sign_in_test_user(self, username, password):
        """
        Method initializes login with random data.
        """
        BrowserHelper.send_keys(self.browser, *LoginPageLocators.USERNAME_FORM, username)
        BrowserHelper.send_keys(self.browser, *LoginPageLocators.PASSWORD_FORM, password)
        BrowserHelper.take_screenshot(self.browser)
        BrowserHelper.click_element(self.browser, *LoginPageLocators.SUBMIT_BUTTON)
