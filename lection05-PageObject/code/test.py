import pytest
import time
from base import BaseCase
from ui.locators import basic_locators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class TestExample(BaseCase):

    @pytest.mark.parametrize(
        'query',
        [
            pytest.param(
              'pycon'
            ),
            pytest.param(
                'python'
            ),
        ],
    )
    @pytest.mark.skip('skip')
    def test_search(self, query):
        self.base_page.search(query)
        assert 'No results found' not in self.driver.page_source

    @pytest.mark.skip('skip')
    def test_negative_search(self):
        self.base_page.search('adasdasdasdasdasda')
        assert 'No results found' not in self.driver.page_source

    @pytest.mark.skip('skip')
    def test_page_change(self):
        self.base_page.click(
            basic_locators.BasePageLocators.GO_BUTTON_LOCATOR, timeout=10
        )

    @pytest.mark.skip('skip')
    def test_carousel(self):
        self.main_page.click(
            basic_locators.MainPageLocators.COMPREHENSIONS, timeout=15
        )

    @pytest.mark.skip('skip')
    def test_iframe(self):
        self.main_page.click(self.main_page.locators.START_SHELL)
        time.sleep(15)
        iframe_first = self.main_page.find((By.XPATH, '//iframe'))
        self.driver.switch_to.frame(iframe_first)
        iframe_second = self.main_page.find((By.ID, 'id_console'))
        self.driver.switch_to.frame(iframe_second)
        iframe = self.main_page.find((By.XPATH, '//iframe'))
        self.driver.switch_to.frame(iframe)
        console = self.main_page.find(self.main_page.locators.PYTHON_CONSOLE)
        console.send_keys('assert 1 == 0')
        console.send_keys(Keys.ENTER)
        time.sleep(10)
        self.driver.switch_to.default_content()
