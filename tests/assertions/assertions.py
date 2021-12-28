import allure
from utils.browser_helper import BrowserHelper

class Assertions:
    @allure.step("Verification of visibility of element")
    def should_be_element(browser, element):
        assert BrowserHelper.find_visible_element(browser, element), "Element is not presented"
    

