from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.XPATH, "//a[contains(@href, '/login')]")

class CreatingFilePageLocators:
    FILE_TEXT_FORM = (By.XPATH, "//div[@id='code-editor']/div/pre")
    COMMIT_NEW_FILE_BUTTON = (By.XPATH, "//button[@id='submit-file']")

class LoginPageLocators:
    USERNAME_FORM = (By.XPATH, "//*[@id='login_field']")
    PASSWORD_FORM = (By.XPATH, "//*[@id='password']")
    SUBMIT_BUTTON = (By.XPATH, "//input[@type='submit']")


class UserMainPageLocators:
    LAST_CREATED_REPOSITORY = (By.XPATH,
                        "//aside[@aria-label='Account']//a[@data-hovercard-type='repository']")

class HeaderUserPageLocators:
    USER_NAME_IN_PROFILE_MENU = (By.XPATH, "//strong[@class='css-truncate-target']")
    USER_ICON = (By.XPATH, "//header//summary//img[contains(@class,'avatar')]")
    DROPDOWN_BUTTON_PROFILE = (By.XPATH,
                                "//summary[@aria-label='View profile and more']//span[@class='dropdown-caret']")
    CREATING_REPOSITORY_BUTTON = (By.XPATH, "//details-menu//a[@href='/new']")
    DROPDOWN_BUTTON_CREATING = (By.XPATH, "//summary[@aria-label='Create new…']")


class NewRepositoryPageLocators:
    REPOSITORY_NAME_FORM = (By.XPATH, "//input[@name='repository[name]']")
    CREATING_BUTTON = (By.XPATH, "//button[contains(text(),'repository')]")

class MainRepositoryPageLocators:
    SETTINGS_REPOSITORY_BUTTON = (By.XPATH, "//a[@id='settings-tab']")
    ACTUAL_REPOSITORY_NAME = (By.XPATH, "//strong[@itemprop='name']/a[@href]")
    ADDING_README_BUTTON = (By.XPATH, "//a[contains(text(),'README')]")
    LAST_COMMIT_TIMESTAMP = (By.XPATH, "//*[@id='repo-content-pjax-container']//time-ago[@datetime]")

class SettingsRepositoryPageLocators:
    DELETE_REPOSITORY_BUTTON = (By.XPATH, "//summary[contains(text(),'Delete this')]")
    CONFIRMATION_DELETE_TEXT = (By.XPATH,
                                "//div[contains(@class,'overflow-auto')]//p[contains(text(),'Please')]/strong")
    CONFIRMATION_FORM = (By.XPATH, "//div[contains(@class,'overflow-auto')]//input[@name='verify']")
    CONFIRMATION_BUTTON = (By.XPATH, "//div[contains(@class,'overflow-auto')]//span[contains(text(),'consequences')]")
    REPOSITORY_NAME_FORM = (By.XPATH, "//*[@id='rename-field']")
    RENAME_CONFIRM_BUTTON = (By.XPATH, "//div[@id='options_bucket']/form/button")
