import allure

from utils.browser_helper import BrowserHelper
from utils.locators import SettingsRepositoryPageLocators
from utils.logger import logger
from .base_page import BasePage
from .header_user_page import HeaderUserPage


class SettingsRepositoryPage(HeaderUserPage, BrowserHelper, BasePage):
    @allure.step("Delete repository")
    def delete_repository(self):
        self.browser.find_element(*SettingsRepositoryPageLocators.DELETE_REPOSITORY_BUTTON).click()
        confirmation_text_input = self.wait_for_element_when_it_become_visible(
            *SettingsRepositoryPageLocators.CONFIRMATION_DELETE_TEXT).text
        self.browser.find_element(*SettingsRepositoryPageLocators.CONFIRMATION_FORM).\
            send_keys(confirmation_text_input)
        self.click_on_element_when_it_become_clickable(*SettingsRepositoryPageLocators.CONFIRMATION_BUTTON)

    @allure.step("Delete repository name in form")
    def delete_repository_name_in_form(self):
        self.browser.find_element(*SettingsRepositoryPageLocators.REPOSITORY_NAME_FORM).clear()

    @allure.step("Change to new repository name in form")
    def change_repository_name_in_form_and_confirm(self):
        input_name = self.generate_new_name()
        self.browser.find_element(*SettingsRepositoryPageLocators.REPOSITORY_NAME_FORM).send_keys(input_name)
        self.click_on_element_when_it_become_clickable(*SettingsRepositoryPageLocators.RENAME_CONFIRM_BUTTON)
