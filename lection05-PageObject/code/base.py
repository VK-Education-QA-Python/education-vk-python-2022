import pytest
from _pytest.fixtures import FixtureRequest
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage

CLICK_RETRY = 3


class BaseCase:
    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.base_page:BasePage = (request.getfixturevalue('base_page'))
        self.main_page:MainPage = (request.getfixturevalue('main_page'))
