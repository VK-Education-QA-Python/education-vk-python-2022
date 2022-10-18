from selenium.webdriver.common.by import By
from ui.pages.base_page import BasePage
from ui.locators.locators_web import SearchPageLocators
from ui.locators.locators_mw import SearchPagePageMWLocators
import allure


class SearchPage(BasePage):
    locators = SearchPageLocators()

    def send_text_to_search_field_and_click_to_element(self, text, desc):
        pass


class SearchPageMW(SearchPage):
    locators = SearchPagePageMWLocators()

    @allure.step("Вводим текст и нажимаем на нужный элемент")
    def send_text_to_search_field_and_click_to_element(self, text, desc):
        self.find(self.locators.SEARCH_FIELD).send_keys(text)
        self.find((By.XPATH, self.locators.ELEMENT_WITH_DESC.format(desc))).click()
