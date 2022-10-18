from ui.pages.base_page import BasePage
from ui.locators.locators_web import LoginLocators
from ui.locators.locators_mw import LoginPageMWLocators
import allure


class LoginPage(BasePage):
    locators = LoginLocators()

    login_url = "https://en.wikipedia.org/w/index.php?title=Special:UserLogin&returnto=Main+Page"

    @allure.step("Авторизовываемся")
    def login(self, login="testusername1090", password="11qazert"):
        self.driver.get(self.login_url)

        self.find(self.locators.LOGIN_FIELD).send_keys(login)
        self.find(self.locators.PASSWORD_FIELD).send_keys(password)
        self.click(self.locators.LOGIN_BUTTON)


class LoginPageMW(LoginPage):
    locators = LoginPageMWLocators()
    login_url = "https://en.m.wikipedia.org/w/index.php?title=Special:UserLogin&returnto=Main+Page"

    @allure.step("Авторизовываемся")
    def login(self, login="testusername1090", password="11qazert"):
        super(LoginPageMW, self).login()


