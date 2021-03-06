import allure
from utils.logger import logger

class BasePage:
    """
    Class for base page of website with URL. URL is defined in class Links module Links.
    """
    def __init__(self, browser, url, timeout=5):
        """
        :param browser: driver instance
        :param url: correct URL for tests
        :param timeout: Time (seconds) for implicitly waiting of any
        find_element methods. Default value - 5 seconds.
        """
        logger.info(f"Initializing the page instance of {url}")
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    @allure.step("Opening the page with link in argument of instance")
    def open(self):
        """
        Method opens the transferred link in initialization method.
        :return: New page with URL.
        """
        logger.info("Opening the page with link by get method")
        self.browser.get(self.url)




