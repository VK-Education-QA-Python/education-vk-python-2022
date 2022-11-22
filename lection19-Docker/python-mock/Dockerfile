FROM python:3.8

ADD requirements.txt /requirements.txt
RUN pip3.8 install -r /requirements.txt

COPY code code

WORKDIR code

CMD ["/code/start_tests.sh"]