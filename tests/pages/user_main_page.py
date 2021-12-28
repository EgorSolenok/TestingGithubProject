import allure

from utils.browser_helper import BrowserHelper
from tests.pages.locators.locators import HeaderUserPageLocators
from tests.pages.locators.locators import UserMainPageLocators
from .base_page import BasePage
from .header_user_page import HeaderUserPage


class UserMainPage(HeaderUserPage, BasePage):
    @allure.step("Go to creating new repository")
    def go_to_creating_new_first_repository_page(self):
        """
        Method goes to page for creating new repository.
        """
        BrowserHelper.click_element(self.browser, *HeaderUserPageLocators.DROPDOWN_BUTTON_CREATING)
        BrowserHelper.click_element(self.browser, *HeaderUserPageLocators.CREATING_REPOSITORY_BUTTON)

    @allure.step("Go to last created repository")
    def go_to_last_repository_page(self):
        """
        Method goes to page with last created repository.
        """
        BrowserHelper.click_element(self.browser, *UserMainPageLocators.LAST_CREATED_REPOSITORY)

    @allure.step("Verify presence of repository for deleting")
    def should_be_repository_for_deleting(self):
        assert BrowserHelper.find_visible_element(self.browser, *UserMainPageLocators.LAST_CREATED_REPOSITORY),\
            "Probably there is no created repositories"