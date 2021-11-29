from .base_page import BasePage
from .locators import LoginPageLocators
from .credentials import Credentials
from utilities.browser_helper import BrowserHelper


class LoginPage(BrowserHelper, BasePage):
    def should_be_login_page(self):
        """
        Complex verification for compliance with the login page. Method is using current URL, verification of
        username and passwords form on th page.
        """
        self.should_be_login_url()
        self.should_be_username_form()
        self.should_be_password_form()

    def should_be_login_url(self):
        assert "github.com/login" in self.browser.current_url, "This page is not login page"

    def should_be_username_form(self):
        assert self.is_element_present(*LoginPageLocators.USERNAME_FORM), "Username form is not presented"

    def should_be_password_form(self):
        assert self.is_element_present(*LoginPageLocators.PASSWORD_FORM), "Password form is not presented"

    def sign_in_test_user(self):
        """
        Method initializes login with data passed in the class Credentials.
        It displays the input data before logging in.
        """
        print(f"Using test login - {Credentials.USERNAME}")
        print(f"Using test password - {Credentials.PASSWORD}")
        self.browser.find_element(*LoginPageLocators.USERNAME_FORM).send_keys(Credentials.USERNAME)
        self.browser.find_element(*LoginPageLocators.PASSWORD_FORM).send_keys(Credentials.PASSWORD)
        self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()
