from ui.pages.base_page import BasePage
from ui.locators.locators_web import TitlePageLocators
from ui.locators.locators_mw import TitlePagePageMWLocators
from ui.locators.locators_android import TitlePageANDROIDLocators
import allure


class TitlePage(BasePage):
    locators = TitlePageLocators()

    def add_to_bookmark(self):
        pass

    def click_on_toolbar_button(self):
        pass

    def click_on_overflow_menu(self):
        pass

    def click_on_overflow_feed(self):
        pass


class TitlePageMW(TitlePage):
    locators = TitlePagePageMWLocators()

    @allure.step("Добавляем статью в избранное")
    def add_to_bookmark(self):
        self.click(self.locators.STAR_BUTTON)


class TitlePageANDROID(TitlePage):
    locators = TitlePageANDROIDLocators()

    def add_to_bookmark(self):
        self.click_for_android(self.locators.MENU_BOOKMARK)

    def click_on_toolbar_button(self):
        self.click_for_android(self.locators.PAGE_TOOLBAR)

    def click_on_overflow_menu(self):
        self.click_for_android(self.locators.OVERFLOW_MENU)

    def click_on_overflow_feed(self):
        self.click_for_android(self.locators.OVERFLOW_FEED)
