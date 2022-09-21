import pytest
import random


@pytest.fixture(scope='function')
def func_fixture():
    yield random.randint(0, 100)


@pytest.fixture(scope='class')
def class_fixture():
    yield random.randint(0, 100)


@pytest.fixture(scope='session')
def session_fixture():
    yield random.randint(0, 100)


@pytest.fixture()
def random_filename():
    return str(random.randint(0, 1000))
