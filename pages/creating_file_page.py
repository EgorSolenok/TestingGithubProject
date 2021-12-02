import allure

from utils.browser_helper import BrowserHelper
from utils.locators import CreatingFilePageLocators
from utils.logger import logger
from .base_page import BasePage
from .header_user_page import HeaderUserPage
from selenium.webdriver.common.keys import Keys


class CreatingFilePage(HeaderUserPage, BrowserHelper, BasePage):
    @allure.step("Write text example in form")
    def write_message_in_file_text(self):
        """
        Method sends in text form message.
        """
        logger.info("Write text example in form")
        information_message = "Initial text for README file"
        self.browser.find_element(*CreatingFilePageLocators.FILE_TEXT_FORM).click()
        self.browser.find_element(*CreatingFilePageLocators.FILE_TEXT_FORM).clear()
        self.browser.find_element(*CreatingFilePageLocators.FILE_TEXT_FORM).send_keys('\n', information_message)

    @allure.step("Commit new file")
    def commit_new_file(self):
        """
        Method commits new file.
        """
        logger.info("Commit new file")
        self.browser.find_element(*CreatingFilePageLocators.COMMIT_NEW_FILE_BUTTON).click()
