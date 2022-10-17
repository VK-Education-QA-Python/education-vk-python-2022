import os

import allure
import pytest
import time

from selenium.webdriver import ActionChains

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
        time.sleep(5)
        self.base_page.search('adasdasdasdasdasda')
        time.sleep(5)
        assert 'No results found' in self.driver.page_source

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

    @pytest.mark.skip('skip')
    def test_new_tab(self):
        current_window = self.driver.current_window_handle

        news = self.main_page.find((By.ID, 'news'))
        ActionChains(self.driver).key_down(Keys.CONTROL).click(news).key_up(Keys.CONTROL).perform()
        time.sleep(5)

        with self.switch_to_window(current=current_window, close=True):
            assert self.driver.current_url == 'https://www.python.org/blogs/'
            time.sleep(3)
        time.sleep(3)

    @pytest.mark.skip('skip')
    def test_events(self):
        time.sleep(5)
        with allure.step('Going to events page'):
            events_page = self.main_page.go_to_events_page()
        time.sleep(5)
        with allure.step('asserting ...'):
            assert 1 == 1

    @pytest.mark.skip('skip')
    def test_relative(self):
        intro = self.main_page.find((By.CSS_SELECTOR, 'div.introduction'))
        learn_more = intro.find_element(*self.main_page.locators.READ_MORE)
        assert learn_more.get_attribute('href') == self.driver.current_url + 'doc/'


class TestLoad(BaseCase):

    @pytest.mark.skip('skip')
    def test_download(self):
        self.driver.get('https://www.python.org/downloads/release/python-3100/')
        time.sleep(5)
        self.main_page.click((By.XPATH, '//a[@href="https://www.python.org/ftp/python/3.10.0/python-3.10.0-embed-win32.zip"]'))
        time.sleep(10)

    @pytest.fixture()
    def file_path(self, repo_root):
        return os.path.join(repo_root, '../files', 'userdata')

    @pytest.mark.skip('skip')
    def test_upload(self, file_path):
        self.driver.get('https://ps.uci.edu/~franklin/doc/file_upload.html')
        input = (By.NAME, 'userfile')
        time.sleep(5)
        self.main_page.find(input).send_keys(file_path)
        time.sleep(5)


class TestFailed(BaseCase):

    @pytest.mark.skip('skip')
    def test_fail(self):
        self.main_page.find((By.XPATH, '12312312312312'), timeout=1)

    @pytest.mark.skip('skip')
    def test_logs_browser(self):
        self.driver.get('https://target.my.com/')
        time.sleep(3)
        assert 0

    @pytest.mark.skip('skip')
    @allure.step("Step 1")
    def test_log(self):
        self.logger.info('Ready to start')
        self.logger.info('Going to events page')
        events_page = self.main_page.go_to_events_page()
        self.logger.info('asserting')
        assert 1 == 1


@pytest.mark.skip('skip')
def test_check_all_drivers(all_drivers):
    time.sleep(3)
