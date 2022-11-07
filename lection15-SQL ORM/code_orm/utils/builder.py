from faker import Faker


class MysqlBuilder:
    def __init__(self, client):
        self.client = client

    def create_banner(self, name=None, url=None):
        fake = Faker()
        banner_name = name or fake.job()
        banner_url = url or fake.url()
        self.client.execute_query(f'insert into `banner` (`name`, `url`) values ("{banner_name}", "{banner_url}")')
