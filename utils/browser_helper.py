import time
from datetime import datetime

import allure
from allure_commons.types import AttachmentType
from loguru import logger
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from utils.logger import LogConfig


class BrowserHelper():
    LogConfig.set_logger_config()

    def highlight(browser, element):
        """
        Highlights (blinks) a Selenium Webdriver element
        """

        def apply_style(style):
            browser.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                                        element, style)

        original_style = element.get_attribute('style')
        apply_style("background: yellow; border: 2px solid red;")
        time.sleep(.05)
        apply_style(original_style)
        

    @allure.step("Verification that element '{1}' is disappeared from page during '{timeout}' seconds")
    def is_disappeared(browser, locator, timeout=3):
        """
        Method that allows you to determine that element is not on the page and does not appear within
        timeout. Default timeout - 3 seconds. How to search (css, id, xpath, etc.). What: selector string.
        True - if element will disappear. False - if element is present.
        """
        logger.info(f"Waiting for element will disappear {locator}")
        try:
            WebDriverWait(browser, timeout, 2, TimeoutException). \
                until_not(expected_conditions.presence_of_element_located(locator))
        except TimeoutException:
            BrowserHelper.take_screenshot(browser)
            logger.error(f"Element {locator} isn't disappeared")
            return False
        return True

    @allure.step("Verification that element '{1}' is not appear  on the page during '{timeout}' seconds")
    def is_not_element_present(browser, locator, timeout=3):
        """
        Method determines the absence of an element on the page over a period of time. Default timeout - 3 seconds.
        how  - how to search (css, id, xpath, etc.). what: selector string.
        timeout: Time to determine absence of element.
        True - if element doesn't exist. False - if element is present.
        """
        logger.info(f"Waiting for element {locator} is not appear during {timeout} seconds")
        try:
            WebDriverWait(browser, timeout).until(expected_conditions.presence_of_element_located(locator))
        except TimeoutException:
            BrowserHelper.take_screenshot(browser)
            logger.error(f"Element {locator} is appeared or was on the page")
            return True
        return False

    @allure.step(f"Waiting for element by '{1}', '{2}' become clickable during {3} seconds and click")
    def click_element(browser, how, what, timeout=5):
        """
        The method click on the element, when it becomes clickable. How: how to search (css, id, xpath, etc.)
        What: Selector string.
        """
        logger.info(f"Waiting for element {how}, '{what}' become clickable for {3} seconds and click")
        clicking_element = WebDriverWait(browser, timeout).until(
            expected_conditions.element_to_be_clickable((how, what)))
        BrowserHelper.highlight(browser, clicking_element)
        clicking_element.click()

    @allure.step(f"Waiting for element '{1}' become visible during {2} seconds")
    def find_visible_element(browser, locator, timeout=3):
        """
        The method wait for the element, when it becomes visible. How: how to search (css, id, xpath, etc.)
        What: Selector string.
        """
        logger.info(f"Waiting for element {locator}' become visible for {3} seconds")
        required_element = WebDriverWait(browser, timeout).until(
            expected_conditions.visibility_of_element_located(locator))
        BrowserHelper.highlight(browser, required_element)
        return required_element

    @allure.step("Send values to the form of element '{1}' '{2}' after clearing")
    def send_keys(browser, how, what, value, timeout=2, clear_first=True, click_first=True):
        required_element = WebDriverWait(browser, timeout).until(
            expected_conditions.element_to_be_clickable((how, what)))
        BrowserHelper.highlight(browser, required_element)
        if click_first:
            logger.info(f"Clicking at element {how} {what}")
            required_element.click()
        if clear_first:
            logger.info(f"Clearing form of {how} {what}")
            required_element.clear()
        logger.info(f"Send values to {how} {what}")
        required_element.send_keys(value)
    
    def take_screenshot(browser):
        with allure.step("Do a screenshot with username"):
            allure.attach(browser.get_screenshot_as_png(),
                          name=f'{str(datetime.now())[2:19].replace(":","-")}', attachment_type=AttachmentType.PNG)
