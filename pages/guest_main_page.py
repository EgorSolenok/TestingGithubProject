from .base_page import BasePage
from utilities.browser_helper import BrowserHelper
from .locators import BasePageLocators

class GuestMainPage(BrowserHelper, BasePage):
    def __init__(self, *args, **kwargs):
        super(GuestMainPage, self).__init__(*args, **kwargs)

    def go_to_login_page(self):
        """
        Method goes to the service login page.
        """
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        """
        The method checks for the presence of a link to go to the login page
        """
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), \
            "Login link is not presented"