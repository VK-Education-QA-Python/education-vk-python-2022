from ui.pages.base_page import BasePage
from ui.locators.locators_web import MainPageLocators
from ui.locators.locators_mw import MainPagePageMWLocators
from ui.locators.locators_android import MainPageANDROIDLocators
import allure


class MainPage(BasePage):
    locators = MainPageLocators()

    def click_on_search_button(self):
        pass

    def open_menu_button(self):
        pass

    def open_watchlist(self):
        pass

    def skip_start_window(self):
        pass

    def click_on_lists_button(self):
        pass


class MainPageMW(MainPage):
    locators = MainPagePageMWLocators()

    @allure.step("Нажимаем на кнопку поиска")
    def click_on_search_button(self):
        self.click(self.locators.SEARCH_ICON)

    @allure.step("Нажимаем на кнопку открытия меню (mobile)")
    def open_menu_button(self):
        self.click(self.locators.MAIN_MENU)

    @allure.step("Нажимаем на кнопку открытия меню (mobile)")
    def open_watchlist(self):
        self.click(self.locators.WATCH_LIST)


class MainPageANDROID(MainPage):
    locators = MainPageANDROIDLocators()

    @allure.step("Пропускаем стартовое окно")
    def skip_start_window(self):
        self.click_for_android(self.locators.SKIP_BUTTON)

    @allure.step("Нажимаем на кнопку поиска")
    def click_on_search_button(self):
        self.click_for_android(self.locators.SEARCH_ICON)

    def click_on_lists_button(self):
        self.click_for_android(self.locators.MY_LISTS)


