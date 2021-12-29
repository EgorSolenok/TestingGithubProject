import allure
import pytest

from tests.assertions.assertions import Assertions
from tests.pages.creating_file_page import CreatingFilePage
from tests.pages.header_user_page import HeaderUserPage
from tests.pages.locators.locators import MainRepoPageLocators
from tests.pages.locators.locators import UserMainPageLocators
from tests.pages.main_repo_page import MainRepoPage
from tests.pages.new_repo_page import NewRepoPage
from tests.pages.settings_repo_page import SettingsRepoPage
from tests.pages.user_main_page import UserMainPage
from utils.generated_data import GeneratedData


@pytest.fixture(scope="function", autouse=True)
def user_page(browser, user, password, guest_main_page, login_page):
    guest_main_page.open()
    guest_main_page.go_to_login_page()
    login_page.sign_in_test_user(user, password)
    user_page = UserMainPage(browser, browser.current_url)
    yield user_page
    current_page = HeaderUserPage(browser, browser.current_url)
    current_page.go_to_dropdown_profile_list()
    current_page.log_out_from_page()



@allure.feature('User main actions with repository')
@allure.severity(allure.severity_level.CRITICAL)
class TestRepositoryMainActions:
    @allure.story("User creates new repository")
    @pytest.mark.main_actions
    @pytest.mark.create_repository
    def test_user_create_new_repository(self, browser, user_page):
        user_page.go_to_creating_new_first_repository_page()
        new_repository_page = NewRepoPage(browser, browser.current_url)
        new_repository_page.create_new_repository()
        Assertions.phrase_should_contain_text(browser, *MainRepoPageLocators.ACTUAL_REPOSITORY_NAME,
                                              phrase=GeneratedData.LAST_GENERATED_NAME)


    @allure.story("User deletes last created repository")
    @pytest.mark.main_actions
    @pytest.mark.delete_repository
    def test_user_delete_last_repository(self, browser, user_page):
        Assertions.should_be_element(browser, *UserMainPageLocators.LAST_CREATED_REPOSITORY)
        user_page.go_to_last_repository_page()
        main_repository_page = MainRepoPage(browser, browser.current_url)
        main_repository_page.go_to_repository_settings()
        settings_page = SettingsRepoPage(browser, browser.current_url)
        settings_page.delete_repository()
        Assertions.elements_should_not_contain_phrase(browser, *UserMainPageLocators.VISIBLE_REPOS,
                                                      phrase=GeneratedData.LAST_GENERATED_NAME)


@allure.feature('User additional actions with repository')
@allure.severity(allure.severity_level.NORMAL)
class TestAdditionRepositoryActions:
    @pytest.fixture(scope="function", autouse=True)
    def repo_page(self, browser, user_page):
        user_page.go_to_creating_new_first_repository_page()
        new_repository_page = NewRepoPage(browser, browser.current_url)
        new_repository_page.create_new_repository()
        repo_page = MainRepoPage(browser, browser.current_url)
        yield repo_page
        main_repository_page = MainRepoPage(browser, browser.current_url)
        main_repository_page.go_to_repository_settings()
        settings_page = SettingsRepoPage(browser, browser.current_url)
        settings_page.delete_repository()

    @allure.story("User rename repository")
    @pytest.mark.addition_actions
    @pytest.mark.rename_repository
    def test_user_rename_repository(self, browser, repo_page):
        repo_page.go_to_repository_settings()
        settings_page = SettingsRepoPage(browser, browser.current_url)
        settings_page.delete_repository_name_in_form()
        settings_page.change_repository_name_in_form_and_confirm()
        Assertions.phrase_should_contain_text(browser, *MainRepoPageLocators.ACTUAL_REPOSITORY_NAME,
                                              phrase=GeneratedData.LAST_GENERATED_NAME)

    @allure.story("User add readme file created repository")
    @pytest.mark.addition_actions
    @pytest.mark.add_readme
    def test_user_add_readme_to_repository(self, browser, repo_page):
        repo_page.go_to_adding_readme_page()
        creating_file_page = CreatingFilePage(browser, browser.current_url)
        creating_file_page.write_message_in_file_text()
        creating_file_page.commit_new_file()
        Assertions.should_be_element(browser, *MainRepoPageLocators.LAST_COMMIT_TIMESTAMP)
