from datetime import datetime

import allure
from allure_commons.types import AttachmentType

from utils.browser_helper import BrowserHelper
from utils.locators import NewRepositoryPageLocators
from .base_page import BasePage
from .header_user_page import HeaderUserPage
from utils.generated_data import GeneratedData


class NewRepositoryPage(HeaderUserPage, BrowserHelper, BasePage):
    @allure.step("Creating new repository")
    def creating_new_repository(self):
        """
        Method create new repository with random name.
        """
        repository_name_input = GeneratedData.generate_new_name()
        repo_name_form = self.browser.find_element(*NewRepositoryPageLocators.REPOSITORY_NAME_FORM)
        repo_name_form.send_keys(repository_name_input)
        allure.attach(self.browser.get_screenshot_as_png(),
                      name=f'Repo_name {(str(datetime.now())[:19])}',
                      attachment_type=AttachmentType.PNG)
        self.click_at_clickable_element(*NewRepositoryPageLocators.CREATING_BUTTON)
