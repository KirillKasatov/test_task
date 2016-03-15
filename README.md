Сервис заказов, используется база данных PostgreSQL
# Некоторые действия:
Клонировать репозиторий (в терминале: git clone git://github.com/KirillKasatov/test_task.git)
#
Создать виртуальное окружение (например, с помощью virtualenvwrapper (в терминале: mkvirtualenv venvname))
#
Находясь в виртуальном окружении, установить необходимые библиотеки с помощью файла requirements.pip,
в каталоге test_task написать в терминале: pip install -r requirements.pip
#
Создать базу данных в PostgreSQL, подключиться к ней, изменив настройки settings.py
#
Загрузить фикстуры для наполнения базы данных (в терминале, в каталоге test_task: python manage.py loaddata fixture.json)
#
Миграции:
#
python manage.py migrate
#
Запуск сервера:
#
python manage.py runserver
#
