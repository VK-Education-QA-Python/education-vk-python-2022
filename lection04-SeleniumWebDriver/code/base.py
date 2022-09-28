import pytest
from ui.locators import basic_locators
from selenium.common.exceptions import StaleElementReferenceException

CLICK_RETRY = 3


class BaseCase:
    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
        self.driver = driver

    def find(self, by, what):
        return self.driver.find_element(by, what)

    def search(self, query):
        search = self.find(*basic_locators.QUERY_LOCATOR)
        search.clear()
        search.send_keys(query)
        go_button = self.find(*basic_locators.GO_BUTTON)
        go_button.click()
        # search.send_keys(Keys.ENTER)

    def click(self, locator):
        for i in range(CLICK_RETRY):
            try:
                elem = self.find(*locator)

                if i < 2:
                    self.driver.refresh()
                elem.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise
