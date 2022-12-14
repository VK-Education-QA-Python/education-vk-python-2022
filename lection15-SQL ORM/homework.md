## Домашнее задание №6 - Backend: MySQL
 
### Цель домашнего задания:
 
- Научиться работать с СУБД из Python
- Получить навыки использования ORM (sqlalchemy)
 
 
### Задача (максимум 7 баллов)
1. Написать в формате тестов код для создания БД и добавления access логов из домашнего задания №5.
2. Все нижеперечисленные действия должны выполняться из Python. Все баллы за задания эквивалентны прошлому ДЗ, за исключением пункта с опцией `--json`
   для python скрипта, т.е. нужно:
   
    2.1. Создать mysql БД для результатов подсчета прямо из тестов, на каждый запуск тестов БД должна пересоздаваться.
    2.2. Переписать скрипт на python из предыдущего домашнего задания в формат тестов pytest, так, чтобы данные по каждому заданию заливались в БД.
    2.3. Каждое задание заливается в отдельную таблицу.
 
3. Проверить работу своего кода нужно по итоговому количеству записей в БД для каждого задания. В идеале - проверять и наполнение.
   То есть, если вам нужно вывести топ-10 записей, то проверяем, что их действительно столько. НЕ ХАРДКОДИТЬ, т.е. мы можем попросить выводить топ-30 записей и т.д.
4. Базу данных поднимаем и настраиваем так же как это делалось в лекции (127.0.0.1:3306, user=root, password=pass). Имя БД - **TEST_SQL**.
 
Условия:
- 100% баллов (7) за задание можно получить только реализовав его по концепции ORM (sqlalchemy).
  При не использовании ORM - максимальный балл 50% (3.5)
- Если задание будет выполнено частично (не все запросы переведены на Python) - это тоже будет принято, но с более низкой оценкой.
 
 
Важные нюансы:
- **ТЕСТЫ ДОЛЖНЫ РАБОТАТЬ в параллельном режиме (-n 2)**.
 
  1. Могут быть проблемы при создании БД - вспоминайте про выполнение каких-то операций только на главном потоке, только на воркерах и т.д.
  Например, не нужно создавать базу данных и таблицы в каждом тесте - это нужно сделать один раз при запуске тестов.
 
  2. Соединение с базой также должно делаться один раз в рамках мастер-потока
  3. Проверяйте, что ваш пайплайн GitHub Actions - зеленый.
- Не забывайте дропать базу после окончания тестов/пересоздавать при запуске тестов, чтобы не оставалось "хвостов".
 
#### Сроки сдачи ДЗ
До 14 ноября включительно.
