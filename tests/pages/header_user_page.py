import allure

from utils.browser_helper import BrowserHelper
from tests.pages.locators.locators import HeaderUserPageLocators
from .base_page import BasePage


class HeaderUserPage(BasePage):
    @allure.step("Click on the dropdown profile list")
    def go_to_dropdown_profile_list(self):
        """
        Method clicks on dropdown profile list
        """
        BrowserHelper.click_element(self.browser, *HeaderUserPageLocators.DROPDOWN_BUTTON_PROFILE)

    @allure.step("Log out from system")
    def log_out_from_page(self):
        """
        Method logs out from system
        """
        BrowserHelper.click_element(self.browser, *HeaderUserPageLocators.LOG_OUT_BUTTON)

    @allure.step("Verification of authorized user icon")
    def should_be_icon_of_authorized_user(self):
        """
        Checking that the user is logged in (by the user icon in header of page).
        """
        assert BrowserHelper.find_visible_element(self.browser, *HeaderUserPageLocators.USER_ICON), \
            "User icon is not presented,probably unauthorised user"

    @allure.step("Should be correct actual name of user")
    def should_be_correct_user(self, user):
        """
        The method checks for the name of actual user with username in credentials.
        """
        self.go_to_dropdown_profile_list()
        actual_user_name = BrowserHelper.find_visible_element(self.browser,
            *HeaderUserPageLocators.USER_NAME_IN_PROFILE_MENU).text
        BrowserHelper.take_screenshot(self.browser)
        assert str(actual_user_name) in f"{user}", "Name of actual user isn't correct"
