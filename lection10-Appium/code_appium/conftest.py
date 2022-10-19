import logging
import sys
import allure
from api.wikipedia import WikipediaApi

from ui.fixtures import *


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')
    parser.addoption('--url', default='https://en.wikipedia.org/')
    parser.addoption('--os', default='web')
    parser.addoption('--debug_log', action='store_true')
    parser.addoption('--appium', default='http://127.0.0.1:4723/wd/hub')


@pytest.fixture(scope='session')
def config(request):
    browser = request.config.getoption('--browser')
    device_os = request.config.getoption('--os')
    appium = request.config.getoption('--appium')
    if device_os == 'mw':
        url = 'https://en.m.wikipedia.org/'
    elif device_os == 'web':
        url = 'https://en.wikipedia.org/'
    else:
        url = request.config.getoption('--url')
    debug_log = request.config.getoption('--debug_log')
    return {'url': url, 'browser': browser, 'device_os': device_os, 'debug_log': debug_log, 'appium': appium}


@pytest.fixture(scope='session')
def repo_root():
    return os.path.abspath(os.path.join(__file__, os.pardir))


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "skip_platform: skip test for necessary platform ",
    )

    if sys.platform.startswith('win'):
        base_test_dir = 'C:\\tests'
    else:
        base_test_dir = '/tmp/tests'

    if not hasattr(config, 'workerinput'):  # execute only once on main worker
        if os.path.exists(base_test_dir):
            shutil.rmtree(base_test_dir)
        os.makedirs(base_test_dir)
        if WikipediaApi().send_request_delete_watchlist() == 200:
            print("===========Watchlist was cleared===========\n")
        else:
            print("===========Watchlist WAS NOT cleared===========\n")

    # save to config for all workers
    config.base_test_dir = base_test_dir


@pytest.fixture(scope='function')
def test_dir(request):
    test_name = request._pyfuncitem.nodeid.replace('/', '_').replace(':', '_')
    test_dir = os.path.join(request.config.base_test_dir, test_name)
    os.makedirs(test_dir)
    return test_dir


@pytest.fixture(scope='function')
def logger(test_dir, config):
    log_formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
    log_file = os.path.join(test_dir, 'test.log')
    log_level = logging.DEBUG if config['debug_log'] else logging.INFO

    file_handler = logging.FileHandler(log_file, 'w')
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(log_level)

    log = logging.getLogger('test')
    log.propagate = False
    log.setLevel(log_level)
    log.handlers.clear()
    log.addHandler(file_handler)

    yield log

    for handler in log.handlers:
        handler.close()


@pytest.fixture(autouse=True)
def skip_by_platform(request, config):
    if request.node.get_closest_marker('skip_platform'):
        if request.node.get_closest_marker('skip_platform').args[0] == config['device_os']:
            pytest.skip('skipped on this platform: {}'.format(config['device_os']))


@pytest.fixture(scope='session', autouse=True)
def add_allure_environment_property(request, config):
    """
    В зависимости от типа девайса добавляем в наши environment аллюра
    environment.properties должен лежать внутри директории файлов allure в виде словаря
    """
    alluredir = request.config.getoption('--alluredir')
    if alluredir:
        env_props = dict()
        if config['device_os'] in ('web', 'mw'):
            env_props['Browser'] = 'Chrome'
        else:
            env_props['Appium'] = '1.20'
            env_props['Android_emulator'] = '11.0'

        if not os.path.exists(alluredir):
            os.makedirs(alluredir)

        allure_env_path = os.path.join(alluredir, 'environment.properties')

        with open(allure_env_path, 'w') as f:
            for key, value in list(env_props.items()):
                f.write(f'{key}={value}\n')
