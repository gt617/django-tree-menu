# Django Tree Menu

Древовидное меню для Django с минимальными зависимостями. Позволяет создавать многоуровневые меню, которые хранятся в базе данных и редактируются через стандартную админку Django.

## Особенности

- неограниченная вложенность пунктов меню
- всего 1 запрос к БД для отрисовки любого меню
- интеграция через template tag
- поддержка явных URL и именованных URL (named URLs)
- активный пункт определяется по URL текущей страницы
- создание меню через админ панель

## Быстрый старт

### Запуск

- Настройка окружения и миграции

```
git clone https://github.com/gt617/django-tree-menu.git
python -m venv venv
source venv/Scripts/activate
pip install requirements.txt
cd project
python manage.py migrate
```
- Создание суперюзера и запуск приложение

```
python manage.py createsuperuser
python manage.py runserver
```