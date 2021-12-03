import allure

from utils.browser_helper import BrowserHelper
from utils.locators import CreatingFilePageLocators
from .base_page import BasePage
from .header_user_page import HeaderUserPage


class CreatingFilePage(HeaderUserPage, BrowserHelper, BasePage):
    @allure.step("Write text example in form")
    def write_message_in_file_text(self):
        """
        Method sends in text form message.
        """
        information_message = "Initial text for README file"
        file_text_form = self.browser.find_element(*CreatingFilePageLocators.FILE_TEXT_FORM)
        file_text_form.click()
        file_text_form.clear()
        file_text_form.send_keys('\n', information_message)


    @allure.step("Commit new file")
    def commit_new_file(self):
        """
        Method commits new file.
        """
        commit_new_file_button = self.browser.find_element(*CreatingFilePageLocators.COMMIT_NEW_FILE_BUTTON)
        commit_new_file_button.click()
