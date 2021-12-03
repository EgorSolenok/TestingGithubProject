import allure

from utils.browser_helper import BrowserHelper
from utils.locators import HeaderUserPageLocators
from utils.locators import UserMainPageLocators
from .base_page import BasePage
from .header_user_page import HeaderUserPage


class UserMainPage(HeaderUserPage, BrowserHelper, BasePage):
    @allure.step("Go to creating new repository")
    def go_to_creating_new_first_repository_page(self):
        """
        Method goes to page for creating new repository.
        """
        self.browser.find_element(*HeaderUserPageLocators.DROPDOWN_BUTTON_CREATING).click()
        self.browser.find_element(*HeaderUserPageLocators.CREATING_REPOSITORY_BUTTON).click()

    @allure.step("Go to last created repository")
    def go_to_last_repository_page(self):
        """
        Method goes to page with last created repository.
        """
        self.click_at_element_when_it_become_visible(*UserMainPageLocators.LAST_CREATED_REPOSITORY)

    @allure.step("Verify presence of repository for deleting")
    def should_be_repository_for_deleting(self):
        assert self.is_element_present(*UserMainPageLocators.LAST_CREATED_REPOSITORY),\
            "Probably there is no created repositories"