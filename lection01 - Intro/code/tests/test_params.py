import pytest


def test_negative():
    errors = []
    for i in range(10):
        try:
            assert i % 2 == 0
        except AssertionError:
            errors.append(f'{i} not even')
    assert not errors


@pytest.mark.parametrize('i', list(range(10)))
def test_even(i):
    """
    :param i: range of integers
    Parametrized test which checks that number if even.
    """
    assert i % 2 == 0


@pytest.mark.parametrize('i, j', [('user', 'test'), ('key', 'value')], ids=['User', 'Key'])
def test_parametrize(i, j):
    """
    :param i: some string
    :param j: and another some string
    Parametrized test which represent parametrize with 2 values and additional IDS in tests naming
    """
    assert i in ['user', 'key']
    assert isinstance(j, str)

