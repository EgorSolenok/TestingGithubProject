import allure

from utils.browser_helper import BrowserHelper
from tests.pages.locators.locators import SettingsRepositoryPageLocators
from .base_page import BasePage
from .header_user_page import HeaderUserPage
from utils.generated_data import GeneratedData


class SettingsRepositoryPage(HeaderUserPage, BasePage):
    @allure.step("Delete repository")
    def delete_repository(self):
        BrowserHelper.click_element(self.browser, *SettingsRepositoryPageLocators.DELETE_REPOSITORY_BUTTON)
        confirmation = BrowserHelper.find_visible_element(self.browser,
            *SettingsRepositoryPageLocators.CONFIRMATION_DELETE_TEXT)
        confirmation_text = confirmation.text
        BrowserHelper.send_keys(self.browser, *SettingsRepositoryPageLocators.CONFIRMATION_FORM, confirmation_text)
        BrowserHelper.click_element(self.browser, *SettingsRepositoryPageLocators.CONFIRMATION_BUTTON)

    @allure.step("Delete repository name in form")
    def delete_repository_name_in_form(self):
        repo_name_form = BrowserHelper.find_visible_element(self.browser, *SettingsRepositoryPageLocators.REPOSITORY_NAME_FORM)
        repo_name_form.clear()

    @allure.step("Change to new repository name in form")
    def change_repository_name_in_form_and_confirm(self):
        input_name = GeneratedData.generate_new_name()
        BrowserHelper.send_keys(self.browser, *SettingsRepositoryPageLocators.REPOSITORY_NAME_FORM, input_name)
        BrowserHelper.click_element(self.browser, *SettingsRepositoryPageLocators.RENAME_CONFIRM_BUTTON)
