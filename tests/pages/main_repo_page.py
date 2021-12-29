import allure

from tests.pages.locators.locators import MainRepoPageLocators
from utils.browser_helper import BrowserHelper
from .base_page import BasePage
from .header_user_page import HeaderUserPage


class MainRepoPage(HeaderUserPage, BasePage):
    @allure.step("Go to repository settings page")
    def go_to_repository_settings(self):
        """
        Method goes to repository settings page.
        """
        BrowserHelper.click_element(self.browser, *MainRepoPageLocators.SETTINGS_REPOSITORY_BUTTON)

    @allure.step("Go to adding README")
    def go_to_adding_readme_page(self):
        """
        Method goes to adding README.
        """
        BrowserHelper.click_element(self.browser, *MainRepoPageLocators.ADDING_README_BUTTON)
