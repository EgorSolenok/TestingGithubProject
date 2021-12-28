import allure

from utils.browser_helper import BrowserHelper
from tests.pages.locators.locators import NewRepositoryPageLocators
from .base_page import BasePage
from .header_user_page import HeaderUserPage
from utils.generated_data import GeneratedData


class NewRepositoryPage(HeaderUserPage, BasePage):
    @allure.step("Creating new repository")
    def creating_new_repository(self):
        """
        Method create new repository with random name.
        """
        repository_name_input = GeneratedData.generate_new_name()
        BrowserHelper.send_keys(self.browser, *NewRepositoryPageLocators.REPOSITORY_NAME_FORM, repository_name_input)
        BrowserHelper.take_screenshot(self.browser)
        BrowserHelper.click_element(self.browser, *NewRepositoryPageLocators.CREATING_BUTTON)
