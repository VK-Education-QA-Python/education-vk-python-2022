import pytest

from test_api.builder import Builder


class ApiBase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, api_client):
        self.api_client = api_client
        self.builder = Builder()

        if self.authorize:
            self.api_client.post_login()

    def check_topic_in_feed(self, topic_id, text):
        found = False
        all_posts_dict = self.api_client.get_feed()
        for posts in all_posts_dict:
            for post in posts:
                if post['object']['id'] == topic_id and post['object']['text'] == text:
                    found = True
                    break
        assert found is True, f'Expected to find topic with id "{topic_id}" and text "{text}" in feed, but got nothing'

    def create_topic(self, title, text, publish=False):
        req = self.api_client.post_topic_create(title=title, text=text, publish=publish)
        assert req['success'] is True

        return req['redirect_url'].split('/')[-2]

    @pytest.fixture(scope='function')
    def topic(self):
        topic_data = self.builder.topic()
        topic_id = self.create_topic(text=topic_data.text, title=topic_data.title, publish=self.publish)
        topic_data.id = topic_id
        yield topic_data

        self.api_client.post_topic_delete(topic_id=topic_id)
