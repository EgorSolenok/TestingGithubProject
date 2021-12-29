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
