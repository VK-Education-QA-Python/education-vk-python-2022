import pytest


@pytest.mark.smoke
@pytest.mark.regress
def test1():
    pass


@pytest.mark.smoke
def test2():
    pass


@pytest.mark.regress
def test3():
    pass