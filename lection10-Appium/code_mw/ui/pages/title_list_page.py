from ui.pages.base_page import BasePage
from ui.locators.locators_web import TitleListPageLocators
from ui.locators.locators_mw import TitleListPagePageMWLocators
from selenium.webdriver.common.by import By
import time
import allure


class TitleListPage(BasePage):
    locators = TitleListPageLocators()

    def check_delete_element_from_saved_title_list(self, text):
        pass


class TitleListPageMW(TitleListPage):
    locators = TitleListPagePageMWLocators()

    def check_delete_element_from_saved_title_list(self, text):
        with allure.step("Нажимаем на 'звездочку'"):
            self.click(self.locators.MARKED_TITLE)
            time.sleep(1)
        with allure.step("Обновляем страницу и нажимаем на оставшуюся статью"):
            self.driver.refresh()
            self.click((By.XPATH, self.locators.TITLE_NAME.format(text)))
        with allure.step("Проверяем, что оставшаяся статья соответствует нужной"):
            self.find((By.XPATH, self.locators.ELEMENT.format(text)))
