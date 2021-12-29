import allure

from utils.browser_helper import BrowserHelper
from tests.pages.locators.locators import NewRepoPageLocators
from .base_page import BasePage
from .header_user_page import HeaderUserPage
from utils.generated_data import GeneratedData


class NewRepoPage(HeaderUserPage, BasePage):
    @allure.step("Creating new repository")
    def create_new_repository(self):
        """
        Method create new repository with random name.
        """
        repository_name_input = GeneratedData.generate_new_name()
        BrowserHelper.send_keys(self.browser, *NewRepoPageLocators.REPOSITORY_NAME_FORM, value=repository_name_input)
        BrowserHelper.take_screenshot(self.browser)
        BrowserHelper.click_element(self.browser, *NewRepoPageLocators.CREATING_BUTTON)
