import pymysql


class MysqlClient:

    def __init__(self, db_name, user, password):
        self.user = 'root'
        self.port = 3306
        self.password = '0000'
        self.host = '127.0.0.1'
        self.db_name = db_name
        self.connection = None

    def connect(self, db_created=True):
        self.connection = pymysql.connect(host=self.host,
                                 port=self.port,
                                 user=self.user,
                                 password=self.password,
                                 db=self.db_name if db_created else None,
                                 charset='utf8',
                                 autocommit=True,
                                 cursorclass=pymysql.cursors.DictCursor
                                 )

    def create_db(self):
        self.connect(db_created=False)
        self.connection.query(f'DROP database IF EXISTS {self.db_name}')
        self.connection.query(f'CREATE database {self.db_name}')

    def create_table_banner(self):
        create_banner = """
        create table `banner`(
            `id` smallint(6) not null auto_increment,
            `name` char(50) not null,
            `url` char(50) not null,
            primary key (`id`)
         )
        """
        self.connection.query(create_banner)

    def execute_query(self, query, fetch=False):
        cursor = self.connection.cursor()
        cursor.execute(query)
        if fetch:
            return cursor.fetchall()
