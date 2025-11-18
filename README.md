# Django Tree Menu

Древовидное меню для Django. Позволяет создавать многоуровневые меню, которые хранятся в базе данных и редактируются через стандартную админку Django.

## Особенности

- неограниченная вложенность пунктов меню
- всего 1 запрос к БД для отрисовки любого меню
- интеграция через template tag
- поддержка явных URL и именованных URL (named URLs)
- активный пункт определяется по URL текущей страницы
- создание меню через админ панель

## Запуск

- Настройка окружения и миграции

```
git clone https://github.com/gt617/django-tree-menu.git
cd django-tree-menu

python -m venv venv
# Linux / macOS
source venv/bin/activate
# Windows
venv\Scripts\activate

pip install -r requirements.txt

cd project
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Как устроено меню

В проекте используется приложение (app) с моделями меню:

- Menu — отдельное меню (например, main_menu)
- MenuItem — пункт меню:
    - menu — к какому меню относится
    - name — название пункта
    - parent — родительский пункт (для вложенности), может быть null
    - simple_url / named_url — явный URL или имя маршрута из urls.py

Структура дерева строится по полю parent

## Использование в шаблоне

```
{% load draw_menu %}
{% draw_menu "main_menu" %}
```
