from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.XPATH, "//a[contains(@href, '/login')]")
    LOGIN_LINK_INVALID = (By.XPATH, "//a[contains(@href, '/LOGIN')]")
    DROPDOWN_BUTTON_PROFILE = (By.XPATH,
                               "//summary[@aria-label='View profile and more']//span[@class='dropdown-caret']")

    USER_ICON = (By.XPATH, "//header//summary//img[contains(@class,'avatar')]")
    USER_NAME_IN_PROFILE_MENU = (By.XPATH, "//strong[@class='css-truncate-target']")


class LoginPageLocators:
    USERNAME_FORM = (By.XPATH, "//*[@id='login_field']")
    PASSWORD_FORM = (By.XPATH, "//*[@id='password']")
    SUBMIT_BUTTON = (By.XPATH, "//input[@type='submit']")
