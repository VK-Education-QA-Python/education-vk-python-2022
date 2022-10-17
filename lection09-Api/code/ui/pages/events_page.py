from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class EventsPage(BasePage):

    locators = basic_locators.EventsPageLocators()
    url = 'https://www.python.org/events/'
