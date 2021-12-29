import allure


class BasePage:
    """
    Class for base page of website with URL. URL is defined in class Links module Links.
    """
    
    def __init__(self, browser, url):
        """
        browser: driver instance. correct URL for tests. Default value - 5 seconds.
        """
        self.browser = browser
        self.url = url
    
    @allure.step("Opening the page with link in argument of instance")
    def open(self):
        """
        Method opens the transferred link in initialization method. New page with URL.
        """
        self.browser.get(self.url)
