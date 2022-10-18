import time
import allure
import pytest
from web_tests.base import BaseCase


class TestWikipediaWeb(BaseCase):
    @pytest.mark.MWUI
    @pytest.mark.UI
    @allure.severity(allure.severity_level.NORMAL)
    @allure.epic("Awesome PyTest framework")
    @allure.title("Test login")
    @allure.description("Test for login")
    @allure.feature('Login tests')
    def test_login(self):
        self.login_page.login()

    @pytest.mark.skip_platform("web")
    def test_saving_two_articles(self):
        text1 = 'Parkway Drive'
        text2 = 'Judas Priest'
        self.login_page.login()
        with allure.step("Нажимаем на кнопку Search и вводим значения в поле ввода"):
            self.main_page.click_on_search_button()
            self.search_page.send_text_to_search_field_and_click_to_element(text1, "Australian metalcore band")
        with allure.step("Добавляем статью в закладки"):
            self.title_page.add_to_bookmark()
            time.sleep(3)
        with allure.step("Нажимаем на кнопку Search и вводим значения в поле ввода"):
            self.main_page.click_on_search_button()
            self.search_page.send_text_to_search_field_and_click_to_element(text2, "British heavy metal band")
        with allure.step("Добавляем статью в закладки"):
            self.title_page.add_to_bookmark()
            time.sleep(3)
        with allure.step("Открываем список избранного"):
            self.main_page.open_menu_button()
            self.main_page.open_watchlist()
        self.title_list_page.check_delete_element_from_saved_title_list(text1)



