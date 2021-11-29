from .base_page import BasePage
from utilities.browser_helper import BrowserHelper
from .locators import BasePageLocators
from .credentials import Credentials


class UserMainPage(BrowserHelper, BasePage):
    def __init__(self, *args, **kwargs):
        super(UserMainPage, self).__init__(*args, **kwargs)

    def go_to_dropdown_profile_list(self):
        """
        :return: Method clicks to dropdown profile menu list
        """
        link = self.browser.find_element(*BasePageLocators.DROPDOWN_BUTTON_PROFILE)
        link.click()

    def should_be_icon_of_authorized_user(self):
        """
        Checking that the user is logged in (by the user icon in header of page).
        """
        assert self.is_element_present(*BasePageLocators.USER_ICON), \
            "User icon is not presented,probably unauthorised user"

    def should_be_correct_user(self):
        """
        The method checks for the name of actual user with username in credentials.
        """
        self.go_to_dropdown_profile_list()
        actual_user = self.browser.find_element(*BasePageLocators.USER_NAME_IN_PROFILE_MENU).text
        assert str(actual_user) in f"{Credentials.USERNAME}", "Name of actual user isn't correct"