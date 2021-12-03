import allure
from datetime import datetime
from allure_commons.types import AttachmentType
from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from utils.logger import logger
from faker import Faker


class BrowserHelper(BasePage):
    LAST_GENERATED_NAME = ''

    @allure.step(f"Verification of the presence of the element {1} and {2}")
    def is_element_present(self, how, what):
        """
        The method that catches the exceptions. How: how to search (css, id, xpath, etc.)
        What: Selector string
        True - if element is on the page, False - if not.
        """
        logger.info(f"Trying to find element {how}, '{what}'")
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            allure.attach(self.browser.get_screenshot_as_png(), name=f'Failure {datetime.now()}',
                          attachment_type=AttachmentType.PNG)
            logger.error(f"Can't find element {how}, '{what}' ")
            return False
        return True

    @allure.step("Generated new fake name")
    @staticmethod
    def generate_new_name():
        new_fake_name = Faker().domain_name()
        BrowserHelper.LAST_GENERATED_NAME = new_fake_name
        logger.info(f"Generated new name {new_fake_name}")
        return new_fake_name

    @allure.step(f"Verification that element {1} {2} is disappeared from page during {3} seconds")
    def is_disappeared(self, how, what, timeout=3):
        """
        Method that allows you to determine that element is not on the page and does not appear within
        timeout. Default timeout - 3 seconds. How to search (css, id, xpath, etc.). What: selector string.
        True - if element will disappear. False - if element is present.
        """
        logger.info(f"Waiting for element will disappear {how}, '{what}'")
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(expected_conditions.presence_of_element_located((how, what)))
        except TimeoutException:
            allure.attach(self.browser.get_screenshot_as_png(), name=f'Failure {datetime.now()}',
                          attachment_type=AttachmentType.PNG)
            logger.error(f"Element {how} {what} isn't disappeared")
            return False
        return True

    @allure.step(f"Verification that element {1} {2} is not appear  on the page during {3} seconds")
    def is_not_element_present(self, how, what, timeout=3):
        """
        Method determines the absence of an element on the page over a period of time. Default timeout - 3 seconds.
        how  - how to search (css, id, xpath, etc.). what: selector string.
        timeout: Time to determine absence of element.
        True - if element doesn't exist. False - if element is present.
        """
        logger.info(f"Waiting for element {how}, {what} is not appear during {timeout} seconds")
        try:
            WebDriverWait(self.browser, timeout).until(expected_conditions.presence_of_element_located((how, what)))
        except TimeoutException:
            allure.attach(self.browser.get_screenshot_as_png(), name=f'Failure {datetime.now()}',
                          attachment_type=AttachmentType.PNG)
            logger.error(f"Element {how} {what} is appeared or was on the page")
            return True
        return False

    @allure.step(f"Waiting for element by '{1}', '{2}' become clickable during {3} seconds and click")
    def click_on_element_when_it_become_clickable(self, how, what, timeout=5):
        """
        The method click on the element, when it becomes clickable. How: how to search (css, id, xpath, etc.)
        What: Selector string.
        """
        logger.info(f"Waiting for element {how}, '{what}' become clickable for {3} seconds and click")
        clicking_element = WebDriverWait(self.browser, timeout).until(
            expected_conditions.element_to_be_clickable((how, what)))
        clicking_element.click()

    @allure.step(f"Waiting for element by '{1}', '{2}' become visible during {3} seconds")
    def wait_for_element_when_it_become_visible(self, how, what, timeout=5):
        """
        The method wait for the element, when it becomes visible. How: how to search (css, id, xpath, etc.)
        What: Selector string.
        """
        logger.info(f"Waiting for element {how}, '{what}' become visible for {3} seconds")
        required_element = WebDriverWait(self.browser, timeout).until(
            expected_conditions.visibility_of_element_located((how, what)))
        return required_element

    @allure.step(f"Clicking at element by '{1}', '{2}' become visible during {3} seconds")
    def click_at_element_when_it_become_visible(self, how, what, timeout=5):
        """
        The method click at the element, when it becomes visible. How: how to search (css, id, xpath, etc.)
        What: Selector string.
        """
        logger.info(f"Clicking at element {how}, '{what}' become visible for {3} seconds")
        required_element = WebDriverWait(self.browser, timeout).until(
            expected_conditions.visibility_of_element_located((how, what)))
        required_element.click()
