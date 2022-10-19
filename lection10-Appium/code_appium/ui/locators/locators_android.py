from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy


class BasePageANDROIDLocators:
    pass


class LoginPageANDROIDLocators(BasePageANDROIDLocators):
    pass


class MainPageANDROIDLocators(BasePageANDROIDLocators):
    SKIP_BUTTON = (By.ID, 'org.wikipedia:id/fragment_onboarding_skip_button')
    SEARCH_ICON = (MobileBy.ACCESSIBILITY_ID, 'Search Wikipedia')
    MY_LISTS = (MobileBy.ACCESSIBILITY_ID, 'My lists')
    # MY_LISTS = (By.XPATH, '//android.widget.FrameLayout[@content-desc="My lists"]/android.widget.ImageView')


class SearchPageANDROIDLocators(BasePageANDROIDLocators):
    SEARCH_FIELD = (MobileBy.ID, 'org.wikipedia:id/search_src_text')
    LIST_ITEM_TITLE = (MobileBy.ID, 'org.wikipedia:id/page_list_item_title')


class TitlePageANDROIDLocators(BasePageANDROIDLocators):
    MENU_BOOKMARK = (MobileBy.ID, 'org.wikipedia:id/article_menu_bookmark')
    PAGE_TOOLBAR = (MobileBy.ID, 'org.wikipedia:id/page_toolbar_button_search')
    OVERFLOW_MENU = (MobileBy.ACCESSIBILITY_ID, 'More options')
    OVERFLOW_FEED = (MobileBy.ID, 'org.wikipedia:id/overflow_feed')


class TitleListPageANDROIDLocators(BasePageANDROIDLocators):
    ITEM_TITLE = (By.ID, 'org.wikipedia:id/item_title')
    FIRST_ELEMENT = (By.XPATH, '//android.view.ViewGroup[2]/android.widget.TextView[1]')
    ELEMENT = "//android.widget.TextView[contains(@text, '{}')][1]"
