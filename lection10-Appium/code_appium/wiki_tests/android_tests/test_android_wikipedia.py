import time
import allure
import pytest
from wiki_tests.base import BaseCase


class TestWikipediaAndroid(BaseCase):

    @pytest.mark.AndroidUI
    def test_skip_start_window(self):
        self.main_page.skip_start_window()

    @pytest.mark.AndroidUI
    def test_saving_two_articles(self):
        text1 = 'Iron Maiden'
        text2 = 'Judas Priest'
        self.main_page.skip_start_window()
        self.main_page.click_on_search_button()
        self.search_page.enter_value_in_search_field_and_click_on_first(text1)
        self.title_page.add_to_bookmark()
        self.title_page.click_on_toolbar_button()
        self.search_page.enter_value_in_search_field_and_click_on_first(text2)
        self.title_page.add_to_bookmark()
        self.title_page.click_on_overflow_menu()
        self.title_page.click_on_overflow_feed()
        self.main_page.click_on_lists_button()
        self.title_list_page.check_delete_element_from_saved_title_list(text2)
