import pytest

from api.client import RespondErrorException
from test_api.base import ApiBase


class TestApi(ApiBase):
    authorize = False

    def test_valid_login(self):
        login_request = self.api_client.post_login()
        assert login_request['bStateError'] is False

    def test_invalid_login(self):
        self.api_client.login = '123'
        self.api_client.password = '456'

        with pytest.raises(RespondErrorException):
            login_request = self.api_client.post_login()
            assert login_request['bStateError'] is True
            pytest.fail(
                f'Unxecpect login happend with login {self.api_client.login} and password {self.api_client.password}')


class TestTopicDraft(ApiBase):
    publish = False

    def test_topic_creation(self, topic):
        print(topic.title)
        print(topic.text)
        print(topic.id)


class TestTopicCreate(TestTopicDraft):
    publish = True

    def test_topic_creation(self, topic):
        print(topic.title)
        self.check_topic_in_feed(text=topic.text, topic_id=topic.id)


#################################################################
# то же самое, другим способом

class TestTopicDraftVer2(ApiBase):
    publish = False

    def check(self):
        print(self.topic.id)

    def test_topic_creation(self, topic):
        self.topic = topic
        self.check()


class TestTopicCreateVer2(TestTopicDraftVer2):
    publish = True

    def check(self):
        self.check_topic_in_feed(text=self.topic.text, topic_id=self.topic.id)
