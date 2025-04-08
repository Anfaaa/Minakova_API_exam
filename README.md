# Задачи API

Это простой API для учета задач в проекте, который поддерживает основные CRUD-операции: создание, чтение, обновление и удаление задач.

## Технологии

- Python 3.x
- Django
- Django REST Framework
- SQLite

## Установка

1. Клонируйте репозиторий:
git clone https://github.com/yourusername/tasks-api.git
2. Перейдите в директорию проекта:
cd tasks-api
3. Установите следующие библиотеки:<br>
Django>=4.2<br>
djangorestframework<br>
drf-yasg<br>
4. Выполните миграции для создания базы данных:
python manage.py migrate
5. Запустите сервер:
python manage.py runserver

Теперь API будет доступен по адресу http://127.0.0.1:8000/.
