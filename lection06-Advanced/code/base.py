from contextlib import contextmanager

import pytest
from _pytest.fixtures import FixtureRequest
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage

CLICK_RETRY = 3


class BaseCase:
    driver = None

    @contextmanager
    def switch_to_window(self, current, close=False):
        for w in self.driver.window_handles:
            if w != current:
                self.driver.switch_to.window(w)
                break
        yield
        if close:
            self.driver.close()
        self.driver.switch_to.window(current)

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.base_page: BasePage = (request.getfixturevalue('base_page'))
        self.main_page: MainPage = (request.getfixturevalue('main_page'))
