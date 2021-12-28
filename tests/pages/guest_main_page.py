import allure

from utils.browser_helper import BrowserHelper
from tests.pages.locators.locators import BasePageLocators
from .base_page import BasePage


class GuestMainPage(BasePage):
    @allure.step("Click on the link to login page")
    def go_to_login_page(self):
        """
        Method goes to service login page
        """
        BrowserHelper.click_element(self.browser, *BasePageLocators.LOGIN_LINK)

    @allure.step("Verification of link to login page")
    def should_be_login_link(self):
        """
        The method checks for the presence of a link to go to the login page
        """
        assert BrowserHelper.find_visible_element(self.browser, *BasePageLocators.LOGIN_LINK), \
            "Login link is not visible"
