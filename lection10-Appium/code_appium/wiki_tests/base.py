import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.pages.search_page import SearchPage
from ui.pages.login_page import LoginPage
from ui.pages.title_page import TitlePage
from ui.pages.title_list_page import TitleListPage


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest, logger, ui_report):
        self.driver = driver
        self.config = config
        self.logger = logger

        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.login_page: LoginPage = request.getfixturevalue('login_page')
        self.main_page: MainPage = request.getfixturevalue('main_page')
        self.search_page: SearchPage = request.getfixturevalue('search_page')
        self.title_page: TitlePage = request.getfixturevalue('title_page')
        self.title_list_page: TitleListPage = request.getfixturevalue('title_list_page')

        self.logger.debug('Initial setup done!')
