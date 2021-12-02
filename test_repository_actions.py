import allure
import pytest

from pages.guest_main_page import GuestMainPage
from utils.links import Links
from pages.login_page import LoginPage
from pages.user_main_page import UserMainPage
from pages.new_repository_page import NewRepositoryPage
from pages.main_repository_page import MainRepositoryPage
from pages.settings_repository_page import SettingsRepositoryPage
from pages.creating_file_page import CreatingFilePage


@pytest.fixture(scope="function", autouse=True)
def setup(browser):
    guest_main_page = GuestMainPage(browser, Links.MAIN_PAGE_LINK)
    guest_main_page.open()
    guest_main_page.go_to_login_page()
    guest_login_page = LoginPage(browser, browser.current_url)
    guest_login_page.sign_in_test_user()


@allure.feature('User main actions with repository')
@allure.severity(allure.severity_level.CRITICAL)
class TestRepositoryMainActions:
    @allure.story("User creates new repository")
    @pytest.mark.main_actions
    @pytest.mark.create_repository
    def test_user_create_new_repository(self, browser):
        user_main_page = UserMainPage(browser, browser.current_url)
        user_main_page.go_to_creating_new_first_repository_page()
        new_repository_page = NewRepositoryPage(browser, browser.current_url)
        new_repository_page.creating_new_repository()
        main_repository_page = MainRepositoryPage(browser, browser.current_url)
        main_repository_page.should_be_correct_repository_name()

    @allure.story("User deletes last created repository")
    @pytest.mark.main_actions
    @pytest.mark.delete_repository
    def test_user_delete_last_repository(self, browser):
        user_main_page = UserMainPage(browser, browser.current_url)
        user_main_page.should_be_repository_for_deleting()
        user_main_page.go_to_last_repository_page()
        main_repository_page = MainRepositoryPage(browser, browser.current_url)
        main_repository_page.go_to_repository_settings()
        settings_page = SettingsRepositoryPage(browser, browser.current_url)
        settings_page.delete_repository()


@allure.feature('User additional actions with repository')
@allure.severity(allure.severity_level.NORMAL)
class TestAdditionRepositoryActions:
    @pytest.fixture(scope="function", autouse=True)
    def setup_for_repository_actions(self, browser):
        user_main_page = UserMainPage(browser, browser.current_url)
        user_main_page.go_to_creating_new_first_repository_page()
        new_repository_page = NewRepositoryPage(browser, browser.current_url)
        new_repository_page.creating_new_repository()
        yield
        main_repository_page = MainRepositoryPage(browser, browser.current_url)
        main_repository_page.go_to_repository_settings()
        settings_page = SettingsRepositoryPage(browser, browser.current_url)
        settings_page.delete_repository()

    @allure.story("User rename repository")
    @pytest.mark.addition_actions
    @pytest.mark.rename_repository
    def test_user_rename_repository(self, browser):
        main_repository_page = MainRepositoryPage(browser, browser.current_url)
        main_repository_page.go_to_repository_settings()
        settings_page = SettingsRepositoryPage(browser, browser.current_url)
        settings_page.delete_repository_name_in_form()
        settings_page.change_repository_name_in_form_and_confirm()
        main_repository_page = MainRepositoryPage(browser, browser.current_url)
        main_repository_page.should_be_correct_repository_name()

    @allure.story("User add readme file created repository")
    @pytest.mark.addition_actions
    @pytest.mark.add_readme
    def test_user_add_readme_to_repository(self, browser):
        main_repository_page = MainRepositoryPage(browser, browser.current_url)
        main_repository_page.go_to_adding_readme_page()
        creating_file_page = CreatingFilePage(browser, browser.current_url)
        creating_file_page.write_message_in_file_text()
        creating_file_page.commit_new_file()
        main_repository_page = MainRepositoryPage(browser, browser.current_url)
        main_repository_page.should_be_created_readme_file()
