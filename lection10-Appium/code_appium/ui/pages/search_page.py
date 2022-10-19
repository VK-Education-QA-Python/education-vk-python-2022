from selenium.webdriver.common.by import By
from ui.pages.base_page import BasePage
from ui.locators.locators_web import SearchPageLocators
from ui.locators.locators_mw import SearchPagePageMWLocators
from ui.locators.locators_android import SearchPageANDROIDLocators
import allure


class SearchPage(BasePage):
    locators = SearchPageLocators()

    def send_text_to_search_field_and_click_to_element(self, text, desc):
        pass

    def enter_value_in_search_field(self, text):
        pass

    def enter_value_in_search_field_and_click_on_first(self, text):
        pass


class SearchPageMW(SearchPage):
    locators = SearchPagePageMWLocators()

    @allure.step("Вводим текст и нажимаем на нужный элемент")
    def send_text_to_search_field_and_click_to_element(self, text, desc):
        self.find(self.locators.SEARCH_FIELD).send_keys(text)
        self.find((By.XPATH, self.locators.ELEMENT_WITH_DESC.format(desc))).click()


class SearchPageANDROID(SearchPage):
    locators = SearchPageANDROIDLocators()

    @allure.step("Вводим значение в поле поиска")
    def enter_value_in_search_field(self, text):
        self.find(self.locators.SEARCH_FIELD).send_keys(text)
        self.driver.hide_keyboard()

    @allure.step("Вводим значение в поле поиска и кликаем на первое")
    def enter_value_in_search_field_and_click_on_first(self, text):
        self.enter_value_in_search_field(text)
        self.click_for_android(self.locators.LIST_ITEM_TITLE)
