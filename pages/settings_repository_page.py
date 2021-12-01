import allure
from datetime import datetime
from allure_commons.types import AttachmentType
from .base_page import BasePage
from .header_user_page import HeaderUserPage
from utils.credentials import Credentials
from utils.locators import BasePageLocators
from utils.locators import HeaderUserPageLocators
from utils.browser_helper import BrowserHelper
from utils.logger import logger
from .new_repository_page import NewRepositoryPage
from utils.locators import MainRepositoryPageLocators
from utils.locators import SettingsRepositoryPageLocators
from utils.credentials import Credentials


class SettingsRepositoryPage(HeaderUserPage, BrowserHelper, BasePage):
    def __init__(self, *args, **kwargs):
        super(SettingsRepositoryPage, self).__init__(*args, **kwargs)

    @allure.step("Delete repository")
    def delete_repository(self):
        logger.info("Delete repository")
        self.browser.find_element(*SettingsRepositoryPageLocators.DELETE_REPOSITORY_BUTTON).click()
        # warning_message = self.browser.switch_to_alert
        # warning_message_output = warning_message.text
        # required_message = warning_message_output.split('type')[1].split('to')[0].strip()
        # print(required_message)
        confirmation_text_input = self.wait_for_element_when_it_become_visible(
            *SettingsRepositoryPageLocators.CONFIRMATION_DELETE_TEXT).text
        logger.info(f"Deleting repository {confirmation_text_input}")
        self.browser.find_element(*SettingsRepositoryPageLocators.CONFIRMATION_FORM).\
            send_keys(confirmation_text_input)
        self.click_on_element_when_it_become_clickable(*SettingsRepositoryPageLocators.CONFIRMATION_BUTTON)