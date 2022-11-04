# Скрипты из лекции:

Скачать образ можно тут:
- https://dev.mysql.com/doc/mysql-installation-excerpt/8.0/en/docker-mysql-getting-started.html#docker-download-image
- https://hub.docker.com/_/mysql

### Запуск бд MySql в контейнере docker
```shell script
docker run --name <name> -p 3306:3306 -e MYSQL_ROOT_PASSWORD=<password> -d mysql:8.0
```
Если образ еще не скачан, то docker автоматически сначала сделает pull из репозитория, а потом запустит.

Проверить статус контейнера:
```shell script
docker ps -a
```
Подключится к клиенту mysql:
```shell script
mysql -h127.0.0.1 -P3306 -uroot -p
```
После окончания работы с БД необходимо остановить контейнер:
```shell script
docker stop <name>
```
Если он больше не нужен, его можно удалить:
```shell script
docker rm <name>
```

### Управление данными в БД:

Просмотр все схем в БД:
```mysql
show databases;
```

Создание новой схемы, выбор схемы для работы и создание таблицы:
```mysql
create database target;
use target;

create table `banner` (
`id` smallint(6) not null auto_increment,
`name` char(20) not null,
`url` char(50) not null,
INDEX USING BTREE (id));

insert into banner values (1, 'reklama', 'vk.com');
```

Пример транзакции с блокировкой:
```mysql
begin;
select name from banner where id =1 for update;
commit;
```
До того как быдет выполена команда commit строка с id=1 будет заблокированна в таблице.
Если в другой сессии попытаться изменить те же данные, то запрос не будет выполнен пока со строки не будет снята блокировка.
Все сессии, которые ждут снятия блокировок можно увидеть тут:
```mysql
SHOW SESSION VARIABLES LIKE "%wait%";
select * from x$innodb_lock_waits;
```

Пример создания таблицы с партиционированием по годам:
```mysql
create table `events` (
`timestamp` timestamp not null,
`date` date not null,
`banner_id` smallint(6) not null,
`event` char(20) not null,
`placement` char(50) not null,
primary key (`date`))
partition by hash(year(`date`));
```

Проверка как именно БД будет выполнять запрос:
```mysql
EXPLAIN ANALYZE SELECT * FROM banner as b JOIN events as e ON (b.id = e.banner_id)
```
Полезно для оптимизации времени выполнения запроса.


### Создание и загрузка дампа с данными:
Для создания дампа используется утилита mysqldump.
```shell script
mysqldump -u root -h 127.0.0.1 -P3306 -p target banner > /tmp/banner.sql
```
Загрузка дампа в БД:
```shell script
mysql -u root -h 127.0.0.1 -P3306 -p target < /tmp/banner.sql
```
