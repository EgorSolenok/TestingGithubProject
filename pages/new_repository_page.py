from datetime import datetime

import allure
from allure_commons.types import AttachmentType

from utils.browser_helper import BrowserHelper
from utils.locators import NewRepositoryPageLocators
from utils.logger import logger
from .base_page import BasePage
from .header_user_page import HeaderUserPage


class NewRepositoryPage(HeaderUserPage, BrowserHelper, BasePage):
    @allure.step("Creating new repository")
    def creating_new_repository(self):
        """
        Method create new repository with random name.
        """
        logger.info("Creating new repository with random repository name")
        repository_name_input = self.generate_new_name()
        self.browser.find_element(*NewRepositoryPageLocators.REPOSITORY_NAME_FORM).send_keys(repository_name_input)
        logger.info("Do a screenshot with repository name")
        allure.attach(self.browser.get_screenshot_as_png(),
                      name=f'Repo_name {(str(datetime.now())[:19])}',
                      attachment_type=AttachmentType.PNG)
        self.click_on_element_when_it_become_clickable(*NewRepositoryPageLocators.CREATING_BUTTON)
