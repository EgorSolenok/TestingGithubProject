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
