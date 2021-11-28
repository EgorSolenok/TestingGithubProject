from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .credentials import Credentials

from .locators import BasePageLocators

"""
Добавляем конструктор, передаем в него экземпляр драйвера и url адресс
Внутри конструктора сохраняем эти данные как аттрибуты нашего класса
:param browser: 
:return:
"""

class BasePage:
    """
    Class for base page of website with URL. URL is defined in class Links module Links.
    """
    def __init__(self, browser, url, timeout=3):
        """
        :param browser: driver instance
        :param url: correct URL for tests
        :param timeout: Time (seconds) for implicitly waiting of any
        find_element methods. Default value - 3 seconds.
        """
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def go_to_login_page(self):
        """
        :return: Method goes to the service login page.
        """
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_dropdown_profile_list(self):
        """
        :return: Method clicks to dropdown profile menu list
        """
        link = self.browser.find_element(*BasePageLocators.DROPDOWN_BUTTON_PROFILE)
        link.click()


    def is_disappeared(self, how, what, timeout=3):
        """
        A method that allows you to determine that an element is not on the page and does not appear within
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

    def is_element_present(self, how, what):
        """
         The method that catches the exception.
        :param how: how to search (css, id, xpath, etc.)
        :param what: Selector string
        :return: True - if element is on the page, False - if not.
        """
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
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

    def open(self):
        """
        Method opens the transferred link in initialization method.
        :return: New page with URL.
        """
        self.browser.get(self.url)

    def should_be_icon_of_authorized_user(self):
        """
        Checking that the user is logged in (by the user icon in header of page).
        """
        assert self.is_element_present(*BasePageLocators.USER_ICON), \
            "User icon is not presented,probably unauthorised user"

    def should_be_login_link(self):
        """
        The method checks for the presence of a link to go to the login page
        """
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), \
            "Login link is not presented"

    def should_be_correct_user(self):
        """
        The method checks for the name of actual user with username in credentials.
        """
        self.go_to_dropdown_profile_list()
        actual_user = self.browser.find_element(*BasePageLocators.USER_NAME_IN_PROFILE_MENU).text
        assert str(actual_user) in f"{Credentials.USERNAME}", "Name of actual user isn't correct"
