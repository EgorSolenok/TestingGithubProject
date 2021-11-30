import allure
from datetime import datetime
from allure_commons.types import AttachmentType
from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BrowserHelper(BasePage):
    @allure.step(f"Verification of the presence of the element {how} {what}")
    def is_element_present(self, how, what):
        """
        The method that catches the exceptions. How: how to search (css, id, xpath, etc.)
        What: Selector string
        True - if element is on the page, False - if not.
        """
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_disappeared(self, how, what, timeout=3):
        """
        A method that allows you to determine that element is not on the page and does not appear within
         timeout. Default timeout - 3 seconds.
        :param how: how to search (css, id, xpath, etc.)
        :param what: Selector string
        :param timeout: The maximum time to determine that an item has disappeared.
        :return: True - if element will disappear. False - if element is present.
        """
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=3):
        """
        Method determines the absence of an element on the page over a period of time. Default timeout - 3 seconds.
        :param how: how to search (css, id, xpath, etc.)
        :param what: Selector string
        :param timeout: Time to determine absence of element.
        :return: True - if element doesn't exist. False - if element is present.
        """
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False