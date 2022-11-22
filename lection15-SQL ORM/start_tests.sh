#!/bin/bash

docker ps -a
pytest -s -l -v  "${TESTS_PATH}" --alluredir /tmp/allure