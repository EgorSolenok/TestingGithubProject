import allure

from utils.browser_helper import BrowserHelper
from utils.locators import SettingsRepositoryPageLocators
from .base_page import BasePage
from .header_user_page import HeaderUserPage
from utils.generated_data import GeneratedData


class SettingsRepositoryPage(HeaderUserPage, BrowserHelper, BasePage):
    @allure.step("Delete repository")
    def delete_repository(self):
        delete_button = self.browser.find_element(*SettingsRepositoryPageLocators.DELETE_REPOSITORY_BUTTON)
        delete_button.click()
        confirmation = self.find_visible_element(
            *SettingsRepositoryPageLocators.CONFIRMATION_DELETE_TEXT)
        confirmation_text = confirmation.text
        confirmation_form = self.browser.find_element(*SettingsRepositoryPageLocators.CONFIRMATION_FORM)
        confirmation_form.send_keys(confirmation_text)
        self.click_at_clickable_element(*SettingsRepositoryPageLocators.CONFIRMATION_BUTTON)

    @allure.step("Delete repository name in form")
    def delete_repository_name_in_form(self):
        repo_name_form = self.browser.find_element(*SettingsRepositoryPageLocators.REPOSITORY_NAME_FORM)
        repo_name_form.clear()

    @allure.step("Change to new repository name in form")
    def change_repository_name_in_form_and_confirm(self):
        input_name = GeneratedData.generate_new_name()
        repo_name_form = self.browser.find_element(*SettingsRepositoryPageLocators.REPOSITORY_NAME_FORM)
        repo_name_form.send_keys(input_name)
        self.click_at_clickable_element(*SettingsRepositoryPageLocators.RENAME_CONFIRM_BUTTON)
