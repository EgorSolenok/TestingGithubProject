import time

import allure

from pages.guest_main_page import GuestMainPage
from utils.links import Links
from pages.login_page import LoginPage
from pages.user_main_page import UserMainPage
from pages.new_repository_page import NewRepositoryPage
from pages.main_repository_page import MainRepositoryPage
from pages.settings_repository_page import SettingsRepositoryPage

@allure.feature('User actions with repository')
@allure.severity(allure.severity_level.NORMAL)
class TestRepositoryActionsFromUserMainPage:
    @allure.story("User creates new repository")
    def test_user_create_new_repository(self, browser):
        guest_main_page = GuestMainPage(browser, Links.MAIN_PAGE_LINK)
        guest_main_page.open()
        guest_main_page.go_to_login_page()
        guest_login_page = LoginPage(browser, browser.current_url)
        guest_login_page.sign_in_test_user()
        user_main_page = UserMainPage(browser, browser.current_url)
        user_main_page.go_to_creating_new_first_repository_page()
        new_repository_page = NewRepositoryPage(browser, browser.current_url)
        new_repository_page.creating_new_repository()
        main_repository_page = MainRepositoryPage(browser, browser.current_url)
        main_repository_page.should_be_correct_repository_name()

    @allure.story("User creates and deletes new repository")
    def test_user_create_and_delete_new_repository(self, browser):
        guest_main_page = GuestMainPage(browser, Links.MAIN_PAGE_LINK)
        guest_main_page.open()
        guest_main_page.go_to_login_page()
        guest_login_page = LoginPage(browser, browser.current_url)
        guest_login_page.sign_in_test_user()
        user_main_page = UserMainPage(browser, browser.current_url)
        user_main_page.go_to_creating_new_first_repository_page()
        new_repository_page = NewRepositoryPage(browser, browser.current_url)
        new_repository_page.creating_new_repository()
        main_repository_page = MainRepositoryPage(browser, browser.current_url)
        main_repository_page.go_to_repository_settings()
        settings_page = SettingsRepositoryPage(browser, browser.current_url)
        settings_page.delete_repository()
        time.sleep(6)

    @allure.story("User deletes last repository")
    def test_user_delete_last_repository(self, browser):
        guest_main_page = GuestMainPage(browser, Links.MAIN_PAGE_LINK)
        guest_main_page.open()
        guest_main_page.go_to_login_page()
        guest_login_page = LoginPage(browser, browser.current_url)
        guest_login_page.sign_in_test_user()
        user_main_page = UserMainPage(browser, browser.current_url)
        user_main_page.go_to_last_repository_page()
        main_repository_page = MainRepositoryPage(browser, browser.current_url)
        main_repository_page.go_to_repository_settings()
        settings_page = SettingsRepositoryPage(browser, browser.current_url)
        settings_page.delete_repository()
        time.sleep(6)
