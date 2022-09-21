import pytest

import random


@pytest.fixture()
def random_value():
    print('entering')
    yield random.randint(0, 100)
    print('exiting')


def test(random_value):
    assert random_value > 50


def test1(func_fixture, session_fixture):
    print(func_fixture, session_fixture)


def test2(func_fixture, session_fixture):
    print(func_fixture, session_fixture)


class Test:
    def test1(self, func_fixture, class_fixture, session_fixture):
        print(func_fixture, class_fixture, session_fixture)

    def test2(self, func_fixture, class_fixture, session_fixture):
        print(func_fixture, class_fixture, session_fixture)

# метод-пустышка, по факту в тестах не использовался, только для примера autouse-фикстуры
# @pytest.fixture(autouse=True)
# def new_file(random_filename):
#     import os
#     f = open(random_filename, 'w')
#     yield
#     f.close()
#     os.remove(random_filename)
