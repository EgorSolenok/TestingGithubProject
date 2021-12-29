import allure

from .base_page import BasePage
from tests.pages.locators.locators import LoginPageLocators
from utils.browser_helper import BrowserHelper


class LoginPage(BasePage):
    @allure.step(f"Signing in")
    def sign_in_test_user(self, username, password):
        """
        Method initializes login with random data.
        """
        BrowserHelper.send_keys(self.browser, *LoginPageLocators.USERNAME_FORM, value=username)
        BrowserHelper.send_keys(self.browser, *LoginPageLocators.PASSWORD_FORM, value=password)
        BrowserHelper.take_screenshot(self.browser)
        BrowserHelper.click_element(self.browser, *LoginPageLocators.SUBMIT_BUTTON)
