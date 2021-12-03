import allure

from utils.browser_helper import BrowserHelper
from utils.locators import BasePageLocators
from utils.logger import logger
from .base_page import BasePage


class GuestMainPage(BrowserHelper, BasePage):
    @allure.step("Click on the link to login page")
    def go_to_login_page(self):
        """
        Method goes to the service login page.
        """
        login_link_button = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link_button.click()
        # with allure.step("Do a screenshot with click on login link page"):
        #     allure.attach(self.browser.get_screenshot_as_png(), name=f'Screenshot {datetime.now()}',
        #                   attachment_type=AttachmentType.PNG)

    @allure.step("Verification of link to login page")
    def should_be_login_link(self):
        """
        The method checks for the presence of a link to go to the login page
        """
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), \
            "Login link is not presented"
