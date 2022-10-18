import os
import shutil
import allure
import pytest
from selenium import webdriver
from ui.pages.base_page import BasePage
from ui import pages
from ui.capability import capability_select

from webdriver_manager.chrome import ChromeDriverManager


class UnsupportedBrowserType(Exception):
    pass


@pytest.fixture
def base_page(driver, config):
    return BasePage(driver=driver, config=config)


@pytest.fixture
def login_page(driver, config):
    page = get_page(config['device_os'], 'LoginPage')
    return page(driver=driver, config=config)


@pytest.fixture
def main_page(driver, config):
    page = get_page(config['device_os'], 'MainPage')
    return page(driver=driver, config=config)


@pytest.fixture
def search_page(driver, config):
    page = get_page(config['device_os'], 'SearchPage')
    return page(driver=driver, config=config)


@pytest.fixture
def title_page(driver, config):
    page = get_page(config['device_os'], 'TitlePage')
    return page(driver=driver, config=config)


@pytest.fixture
def title_list_page(driver, config):
    page = get_page(config['device_os'], 'TitleListPage')
    return page(driver=driver, config=config)


def get_page(device, page_class):
    if device == 'mw':
        page_class += "MW"
    page = getattr(pages, page_class, None)
    if page is None:
        raise Exception(f'No such page {page_class}')
    return page


def get_driver(browser_name, device_os):
    manager = ChromeDriverManager(version='106.0.5249.21')
    if device_os == 'web':
        if browser_name == 'chrome':
            browser = webdriver.Chrome(executable_path=manager.install(),
                                       options=capability_select(device_os))
        else:
            raise UnsupportedBrowserType(f' Unsupported browser {browser_name}')
    elif device_os == 'mw':
        browser = webdriver.Chrome(executable_path=manager.install(),
                                   options=capability_select(device_os))
    else:
        raise UnsupportedBrowserType(f' Unsupported device_os type {device_os}')
    return browser


@pytest.fixture(scope='function')
def driver(config, test_dir):
    url = config['url']
    browser_name = config['browser']
    device_os = config['device_os']
    browser = get_driver(browser_name, device_os)
    browser.get(url)
    yield browser
    browser.quit()


@pytest.fixture(scope='function')
def ui_report(driver, request, test_dir):
    failed_tests_count = request.session.testsfailed
    yield
    if request.session.testsfailed > failed_tests_count:
        screenshot_file = os.path.join(test_dir, 'failure.png')
        driver.get_screenshot_as_file(screenshot_file)
        allure.attach.file(screenshot_file, 'failure.png', attachment_type=allure.attachment_type.PNG)

        browser_logfile = os.path.join(test_dir, 'browser.log')
        with open(browser_logfile, 'w') as f:
            for i in driver.get_log('browser'):
                f.write(f"{i['level']} - {i['source']}\n{i['message']}\n\n")

        with open(browser_logfile, 'r') as f:
            allure.attach(f.read(), 'browser.log', attachment_type=allure.attachment_type.TEXT)
