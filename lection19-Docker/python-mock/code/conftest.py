import os
import signal
import subprocess
import time
from copy import copy

import requests

import settings

repo_root = os.path.abspath(os.path.join(__file__, os.pardir))


def wait_ready(host, port):
    started = False
    st = time.time()
    while time.time() - st <= 5:
        try:
            requests.get(f'http://{host}:{port}')
            started = True
            break
        except ConnectionError:
            pass

    if not started:
        raise RuntimeError('App did not started in 5s!')


def pytest_configure(config):

    if not hasattr(config, 'workerinput'):
        ######### app configuration #########

        app_path = os.path.join(repo_root, 'application', 'app.py')

        env = copy(os.environ)
        env.update({'APP_HOST': settings.APP_HOST, 'APP_PORT': settings.APP_PORT})
        env.update({'STUB_HOST': settings.STUB_HOST, 'STUB_PORT': settings.STUB_PORT})
        env.update({'MOCK_HOST': settings.MOCK_HOST, 'MOCK_PORT': settings.MOCK_PORT})


        app_stderr = open('/tmp/stub_stderr', 'w')
        app_stdout = open('/tmp/stub_stdout', 'w')
        # windows
        # app_stderr_path = os.path.join(repo_root, 'tmp', 'app_stderr')
        # app_stdout_path = os.path.join(repo_root, 'tmp', 'app_stdout')
        # app_stderr = open(app_stderr_path, 'w')
        # app_stdout = open(app_stdout_path, 'w')
        app_proc = subprocess.Popen(['python3', app_path], stderr=app_stderr, stdout=app_stdout, env=env)
        # windows
        # app_proc = subprocess.Popen(['c:\\tp\\venv\\Scripts\\python', app_path],
        #                             stderr=app_stderr, stdout=app_stdout, env=env
        #                             )
        config.app_proc = app_proc
        config.app_stderr = app_stderr
        config.app_stdout = app_stdout
        wait_ready(settings.APP_HOST, settings.APP_PORT)

        ######### stub configuration #########

        # stub_path = os.path.join(repo_root, 'stub', 'flask_stub.py')
        stub_path = os.path.join(repo_root, 'stub', 'simple_http_server_stub.py')

        env = copy(os.environ)
        env.update({'APP_HOST': settings.STUB_HOST, 'APP_PORT': settings.STUB_PORT})

        stub_stderr = open('/tmp/stub_stderr', 'w')
        stub_stdout = open('/tmp/stub_stdout', 'w')
        # windows
        # stub_stderr_path = os.path.join(repo_root, 'tmp', 'stub_stderr')
        # stub_stdout_path = os.path.join(repo_root, 'tmp', 'stub_stdout')
        # stub_stderr = open(stub_stderr_path, 'w')
        # stub_stdout = open(stub_stdout_path, 'w')

        # stub_proc = subprocess.Popen(['c:\\tp\\venv\\Scripts\\python', stub_path],
        stub_proc = subprocess.Popen(['python3', app_path],
                                     stderr=stub_stderr, stdout=stub_stdout, env=env
                                     )
        import time; time.sleep(2)
        config.stub_proc = stub_proc
        config.stub_stderr = stub_stderr
        config.stub_stdout = stub_stdout
        wait_ready(settings.STUB_HOST, settings.STUB_PORT)


        ######### mock configuration #########

        from mock import flask_mock
        flask_mock.run_mock()

        wait_ready(settings.MOCK_HOST, settings.MOCK_PORT)


def pytest_unconfigure(config):
    # config.proc.send_signal(signal.SIGINT)
    # exit_code = config.proc.wait()
    # assert exit_code == 0

    config.app_proc.terminate()
    exit_code = config.app_proc.wait()

    config.app_stderr.close()
    config.app_stdout.close()

    assert exit_code == -15

    config.stub_proc.terminate()
    exit_code = config.stub_proc.wait()

    config.stub_stderr.close()
    config.stub_stdout.close()

    assert exit_code == -15

    # TODO: add mock shutdown
    requests.get(f'http://{settings.MOCK_HOST}:{settings.MOCK_PORT}/shutdown')
