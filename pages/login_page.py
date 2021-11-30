import allure
from datetime import datetime
from allure_commons.types import AttachmentType
from .base_page import BasePage
from utils.locators import LoginPageLocators
from utils.credentials import Credentials
from utils.browser_helper import BrowserHelper
from utils.logger import logger



class LoginPage(BrowserHelper, BasePage):
    @allure.step("Verification of login page (correct URL, username and password forms")
    def should_be_login_page(self):
        """
        Complex verification for compliance with the login page. Method is using current URL, verification of
        username and passwords form on th page.
        """
        logger.info("Verification of login page (correct URL, username and password forms")
        self.should_be_login_url()
        self.should_be_username_form()
        self.should_be_password_form()

    @allure.step("Verification of correct URL of login page")
    def should_be_login_url(self):
        logger.info("Verification of correct URL of login page")
        assert "github.com/login" in self.browser.current_url, "This page is not login page"

    @allure.step("Verification of username form")
    def should_be_username_form(self):
        logger.info("Verification of correct URL of login page")
        assert self.is_element_present(*LoginPageLocators.USERNAME_FORM), "Username form is not presented"

    @allure.step("Verification of password form")
    def should_be_password_form(self):
        logger.info("Verification of password form")
        assert self.is_element_present(*LoginPageLocators.PASSWORD_FORM), "Password form is not presented"

    @allure.step(f"Sign in with given credentials {Credentials.USERNAME} {Credentials.PASSWORD}")
    def sign_in_test_user(self):
        """
        Method initializes login with data passed in the class Credentials.
        It displays the input data before logging in.
        """
        logger.info(f"Sign in with given credentials {Credentials.USERNAME} {Credentials.PASSWORD}")
        self.browser.find_element(*LoginPageLocators.USERNAME_FORM).send_keys(Credentials.USERNAME)
        self.browser.find_element(*LoginPageLocators.PASSWORD_FORM).send_keys(Credentials.PASSWORD)
        with allure.step("Do a screenshot with credentials"):
            logger.info("Do a screenshot with credentials")
            allure.attach(self.browser.get_screenshot_as_png(),
                          name=f'Cred_sign_in {(str(datetime.now())[:19])}',
                          attachment_type=AttachmentType.PNG)
        self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()
