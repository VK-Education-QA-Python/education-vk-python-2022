from base import BaseCase
import pytest
from ui.locators import basic_locators


class TestOne(BaseCase):
    @pytest.mark.parametrize(
        'query',
        [
            pytest.param(
                'pycon'
            ),
            pytest.param(
                'python'
            )
        ]
    )
    @pytest.mark.skip("SKIP")
    def test(self, query):
        assert "Python" in self.driver.title
        self.search(query=query)
        assert "No results found." not in self.driver.page_source

    def test_page_change(self):
        self.click(locator=basic_locators.GO_BUTTON)
