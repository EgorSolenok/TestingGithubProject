import allure
from datetime import datetime
from allure_commons.types import AttachmentType
from .base_page import BasePage
from utils.credentials import Credentials
from utils.locators import BasePageLocators
from utils.browser_helper import BrowserHelper
from utils.logger import logger


class UserMainPage(BrowserHelper, BasePage):
    def __init__(self, *args, **kwargs):
        super(UserMainPage, self).__init__(*args, **kwargs)

    @allure.step("Click on the dropdown profile list")
    def go_to_dropdown_profile_list(self):
        """
        Method clicks on dropdown profile list
        """
        logger.info("Click on the dropdown profile list")
        dropdown_list_link = self.browser.find_element(*BasePageLocators.DROPDOWN_BUTTON_PROFILE)
        dropdown_list_link.click()



    @allure.step("Verification of authorized user icon")
    def should_be_icon_of_authorized_user(self):
        """
        Checking that the user is logged in (by the user icon in header of page).
        """
        logger.info("Verification of authorized user icon")
        assert self.is_element_present(*BasePageLocators.USER_ICON), \
            "User icon is not presented,probably unauthorised user"

    @allure.step("Should be correct actual name of user")
    def should_be_correct_user(self):
        """
        The method checks for the name of actual user with username in credentials.
        """
        self.go_to_dropdown_profile_list()
        logger.info("Definition of actual user name in dropdown profile list")
        actual_user_name = self.browser.find_element(*BasePageLocators.USER_NAME_IN_PROFILE_MENU).text
        with allure.step("Do a screenshot with profile list"):
            logger.info("Do a screenshot with profile list")
            allure.attach(self.browser.get_screenshot_as_png(),
                          name=f'Scr_menu {(str(datetime.now())[:19])}',
                          attachment_type=AttachmentType.PNG)
        logger.info("Verification of actual user name by data comparison from credentials")
        assert str(actual_user_name) in f"{Credentials.USERNAME}", "Name of actual user isn't correct"