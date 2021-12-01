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
from utils.locators import UserMainPageLocators

class UserMainPage(HeaderUserPage, BrowserHelper, BasePage):
    def __init__(self, *args, **kwargs):
        super(UserMainPage, self).__init__(*args, **kwargs)

    @allure.step("Go to creating new repository")
    def go_to_creating_new_first_repository_page(self):
        """
        Method goes to page for creating new repository.
        """
        logger.info("Go to creating new repository")
        self.browser.find_element(*HeaderUserPageLocators.DROPDOWN_BUTTON_CREATING).click()
        self.browser.find_element(*HeaderUserPageLocators.CREATING_REPOSITORY_BUTTON).click()

    @allure.step("Go to last created repository")
    def go_to_last_repository_page(self):
        """
        Method goes to page with last created repository.
        """
        logger.info("Go to last created repository")
        self.wait_for_element_when_it_become_visible(*UserMainPageLocators.LAST_CREATED_REPOSITORY).click()

    # @allure.step("Go to adding new repository")
    # def go_to_adding_new_repository_page(self):
    #     """
    #     Method goes to page for creating new repository. Method is implemented for the case when
    #     there are no other repositories.
    #     """
    #     logger.info("Go to adding new repository")
    #     self.browser.find_element(*HeaderUserPageLocators.ADD_NEW_REPOSITORY_BUTTON).click()

