import sys


def pytest_addoption(parser):
    parser.addoption('--env', type=str, default='prod')


def is_master(config):
    if hasattr(config, 'workerinput'):
        return False
    return True


def pytest_configure(config):
    if is_master(config):
        print('This is configure hook on MASTER\n')
    else:
        sys.stderr.write(f'This is configure hook on WORKER {config.workerinput["workerid"]}\n')


def pytest_unconfigure(config):
    if is_master(config):
        print('This is unconfigure hook on MASTER\n')
    else:
        sys.stderr.write(f'This is unconfigure hook on WORKER {config.workerinput["workerid"]}\n')
