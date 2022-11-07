import pymysql

connection = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='0000',
    db=None,
    charset='utf8',
)
connection.query('drop database if exists `target`')
connection.query('create database target;')
connection.close()

connection = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='0000',
    db='target',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor,
    autocommit=True
)

text_query='create table banner (`id` smallint(10) not null auto_increment, `name` char(50) not null, `url` varchar(50) not null, primary key (`id`))'
connection.query(text_query)

connection.query('insert into `banner` values (1 , "test name", "vk.com")')

res = connection.query('select * from `banner`;')
print(res)


cursor = connection.cursor()
cursor.execute('select * from `banner`;')

res_2 = cursor.fetchall()
print(res_2)

connection.close()
