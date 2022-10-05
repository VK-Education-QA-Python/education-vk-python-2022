from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from ui.pages.events_page import EventsPage


class MainPage(BasePage):

    locators = basic_locators.MainPageLocators()

    def go_to_events_page(self):
        events_button = self.find(self.locators.EVENTS)
        events_button.click()
        return EventsPage(self.driver)
