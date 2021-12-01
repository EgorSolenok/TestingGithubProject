import allure
from datetime import datetime
from allure_commons.types import AttachmentType
from utils.logger import logger
from .base_page import BasePage
from .user_main_page import UserMainPage
from .header_user_page import HeaderUserPage
from faker import Faker
from utils.browser_helper import BrowserHelper
from utils.locators import BasePageLocators
from utils.locators import NewRepositoryPageLocators
from utils.credentials import Credentials
import time


class NewRepositoryPage(HeaderUserPage, BrowserHelper, BasePage):
    def __init__(self, *args, **kwargs):
        super(NewRepositoryPage, self).__init__(*args, **kwargs)

    @allure.step("Creating new repository")
    def creating_new_repository(self):
        """
        Method create new repository with random name.
        """
        logger.info("Creating new repository with random repository name")
        repository_name_input = Credentials.FAKE_REPOSITORY_NAME
        self.browser.find_element(*NewRepositoryPageLocators.REPOSITORY_NAME_FORM).send_keys(repository_name_input)
        logger.info("Do a screenshot with repository name")
        allure.attach(self.browser.get_screenshot_as_png(),
                      name=f'Repo_name {(str(datetime.now())[:19])}',
                      attachment_type=AttachmentType.PNG)
        self.click_on_element_when_it_become_clickable(*NewRepositoryPageLocators.CREATING_BUTTON)



