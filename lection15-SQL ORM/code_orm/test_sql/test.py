import pytest
from mysql.client import MysqlClient
from utils.builder import MysqlBuilder
from models.banner import BannerModel


class MyTest:

    def prepare(self):
        pass

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client):
        self.client:MysqlClient = mysql_client
        self.builder: MysqlBuilder = MysqlBuilder(self.client)
        self.prepare()

    def get_banners(self, **filters):
        self.client.session.commit()
        return self.client.session.query(BannerModel).filter_by(**filters).all()


class TestMysql(MyTest):

    def prepare(self):
        self.builder.create_banner()

    def test(self):
        banners = self.get_banners()
        assert len(banners) == 1
