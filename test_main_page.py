import allure
import pytest
import time
from pages.guest_main_page import GuestMainPage
from pages.login_page import LoginPage
from pages.user_main_page import UserMainPage
from pages.links import Links
from selenium import webdriver

@allure.feature('Guest actions on the main page')
class TestLoginFromMainPage:
    @allure.story('Guest see link to sign in')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_guest_should_see_login_link(self, browser):
        page = GuestMainPage(browser, Links.MAIN_PAGE_LINK)
        page.open()
        page.should_be_login_link()

    @allure.story('Guest can click on the link to sign in')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_guest_can_go_to_login_page(self, browser):
        page = GuestMainPage(browser, Links.MAIN_PAGE_LINK)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    @allure.story('Guest can click on the link and sign in')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_guest_can_sign_in_test_user(self, browser):
        page = GuestMainPage(browser, Links.MAIN_PAGE_LINK)
        page.open()
        page.go_to_login_page()
        page = LoginPage(browser, browser.current_url)
        page.should_be_login_page()
        page.sign_in_test_user()
        page = UserMainPage(browser, browser.current_url)
        page.should_be_icon_of_authorized_user()
        page.should_be_correct_user()
