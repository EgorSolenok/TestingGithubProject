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
from utils.credentials import Credentials


class MainRepositoryPage(HeaderUserPage, BrowserHelper, BasePage):
    def __init__(self, *args, **kwargs):
        super(MainRepositoryPage, self).__init__(*args, **kwargs)

    @allure.step(f"Verification of actual repo name by data comparison from credentials ")
    def should_be_correct_repository_name(self):
        """
        Method verifies the actual name of repository with random name given in credentials.
        """
        actual_repository_name = self.browser.find_element(*MainRepositoryPageLocators.ACTUAL_REPOSITORY_NAME).text
        logger.info(f"Verification of actual repo name {actual_repository_name} by"
                    f" data comparison from credentials - {Credentials.FAKE_REPOSITORY_NAME}")
        assert str(actual_repository_name) in f"{Credentials.FAKE_REPOSITORY_NAME}",\
            "Name of actual repo isn't correct"

    @allure.step("Go to repository settings page")
    def go_to_repository_settings(self):
        """
        Method goes to repository settings page.
        """
        logger.info("Go to repository settings page")
        self.browser.find_element(*MainRepositoryPageLocators.SETTINGS_REPOSITORY_BUTTON).click()
