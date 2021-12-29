import allure
from utils.browser_helper import BrowserHelper

class Assertions:
    @allure.step("Verification of visibility '{1}' element")
    def should_be_element(browser, *locator):
        required_element = BrowserHelper.find_visible_element(browser, *locator)
        assert required_element, "Element is not presented"
        
    @allure.step("Verification of correct URL of page")
    def should_be_correct_url(browser, url_identifier=str):
        assert f"{url_identifier}" in browser.current_url, "Url of that page don't contains url phrase"
        
    def phrase_should_contain_text(browser, *locator, phrase=str):
        required_element = BrowserHelper.find_visible_element(browser, *locator)
        actual_text = required_element.text
        assert actual_text in f"{phrase}", "Actual text of element isn't part of given phrase"
        
    def elements_should_not_contain_phrase(browser, *locator, phrase=str):
        required_elements = BrowserHelper.find_visible_elements(browser, *locator)
        for element in required_elements:
            assert phrase not in element.text, "Element contain phrase but should not"

    

