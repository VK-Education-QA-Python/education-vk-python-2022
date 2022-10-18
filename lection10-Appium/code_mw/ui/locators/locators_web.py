from selenium.webdriver.common.by import By


class BasePageLocators:
    pass


class LoginLocators(BasePageLocators):
    LOGIN_FIELD = (By.ID, 'wpName1')
    PASSWORD_FIELD = (By.ID, 'wpPassword1')
    LOGIN_BUTTON = (By.ID, 'wpLoginAttempt')


class MainPageLocators(BasePageLocators):
    pass


class SearchPageLocators(BasePageLocators):
    pass


class TitlePageLocators(BasePageLocators):
    pass


class TitleListPageLocators(BasePageLocators):
    pass
