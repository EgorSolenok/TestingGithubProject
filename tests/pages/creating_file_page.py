import allure

from tests.pages.locators.locators import CreatingFilePageLocators
from utils.browser_helper import BrowserHelper
from .base_page import BasePage
from .header_user_page import HeaderUserPage


class CreatingFilePage(HeaderUserPage, BasePage):
    @allure.step("Write text example in form")
    def write_message_in_file_text(self):
        """
        Method sends in text form message.
        """
        information_message = "Initial text for README file"
        BrowserHelper.send_keys(self.browser, *CreatingFilePageLocators.FILE_TEXT_FORM, information_message)


    @allure.step("Commit new file")
    def commit_new_file(self):
        """
        Method commits new file.
        """
        BrowserHelper.click_element(self.browser, *CreatingFilePageLocators.COMMIT_NEW_FILE_BUTTON)
