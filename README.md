## blog
#### Скачать зависимости pip -r requirements.txt
#### Создать миграции python manage.py makemigrations
#### Применить миграции python manage.py migrate
#### Создать супер-пользователя python manage.py createsuperuser

### Блоги и комментарии создаются в админке.
### http://127.0.0.1:8000/api/ - Все блоги
### http://127.0.0.1:8000/api/<str:pk>/ - Детально блог,уровень вложенности комментариев не больше 3 передаем id-блога
### http://127.0.0.1:8000/api/<str:pk>/<str:lvl>/ - id-блога, уровень комментариев который нужно посмотреть. 
