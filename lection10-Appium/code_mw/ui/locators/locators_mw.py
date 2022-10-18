from selenium.webdriver.common.by import By


class BasePageMWLocators:
    pass


class LoginPageMWLocators(BasePageMWLocators):
    LOGIN_FIELD = (By.ID, 'wpName1')
    PASSWORD_FIELD = (By.ID, 'wpPassword1')
    LOGIN_BUTTON = (By.ID, 'wpLoginAttempt')


class MainPagePageMWLocators(BasePageMWLocators):
    MAIN_MENU = (By.ID, 'mw-mf-main-menu-button')
    WATCH_LIST = (By.XPATH, "//span[text()='Watchlist']")												 
    SEARCH_ICON = (By.ID, 'searchIcon')


class SearchPagePageMWLocators(BasePageMWLocators):
    SEARCH_FIELD = (By.XPATH, '//input[@class="search mw-ui-background-icon-search"]')
    ELEMENT_WITH_DESC = '//div[text()="{}"]'


class TitlePagePageMWLocators(BasePageMWLocators):
    STAR_BUTTON = (By.ID, 'ca-watch')


class TitleListPagePageMWLocators(BasePageMWLocators):
    MARKED_TITLE = (By.XPATH, "//a[contains(@class,'icon-wikimedia-unStar-progressive')]")
    TITLE_NAME = "//h3[text()='{}']"
    ELEMENT = "//span[text()='{}']"
