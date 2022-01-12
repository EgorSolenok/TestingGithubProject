import time
from datetime import datetime

import allure
from allure_commons.types import AttachmentType
from loguru import logger
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from utils.logger import LogConfig


class BrowserHelper():
    # Set required config for project logger
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
    def is_disappeared(browser, *locator, timeout=3):
        """
        Method that allows you to determine that element is not on the page and does not appear within
        timeout. True - if element will disappear. False - if element is present.
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
    def is_not_element_present(browser, *locator, timeout=3):
        """
        Method determines the absence of an element on the page over a period of time.
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

    @allure.step("Click at clickable element '{1}'")
    def click_element(browser, *locator, timeout=5):
        """
        The method click on the element, when it becomes clickable. How: how to search (css, id, xpath, etc.)
        What: Selector string.
        """
        logger.info(f"Waiting for element {locator}' become clickable for {timeout} seconds and click")
        clicking_element = WebDriverWait(browser, timeout).until(
            expected_conditions.element_to_be_clickable(locator))
        BrowserHelper.highlight(browser, clicking_element)
        clicking_element.click()

    @allure.step("Waiting for element '{1}' become visible during '{2}'seconds")
    def find_visible_element(browser, *locator, timeout=3):
        """
        The method wait for the element, when it becomes visible.
        """

        required_element = WebDriverWait(browser, timeout).until(
            expected_conditions.visibility_of_element_located((locator)))
        BrowserHelper.highlight(browser, required_element)
        return required_element
    
    @allure.step("Waiting for elements '{1}' become visible during '{2}'seconds")
    def find_visible_elements(browser, *locator, timeout=3):
        """
        The method wait for the elements, when them becomes visible. How: how to search (css, id, xpath, etc.)
        """
        required_elements = WebDriverWait(browser, timeout).until(
            expected_conditions.visibility_of_all_elements_located((locator)))
        return required_elements

    @allure.step("Send values to the form of element '{locator}' after clearing")
    def send_keys(browser, *locator, value=None, timeout=2, clear_first=True, click_first=True):
        required_element = WebDriverWait(browser, timeout).until(
            expected_conditions.element_to_be_clickable(locator))
        BrowserHelper.highlight(browser, required_element)
        if click_first:
            logger.info(f"Clicking at element {locator}")
            required_element.click()
        if clear_first:
            logger.info(f"Clearing form of {locator}")
            required_element.clear()
        logger.info(f"Send values to {locator}")
        required_element.send_keys(value)
    
    def take_screenshot(browser):
        with allure.step("Do a screenshot with username"):
            allure.attach(browser.get_screenshot_as_png(),
                          name=f'{str(datetime.now())[2:19].replace(":","-")}', attachment_type=AttachmentType.PNG)
