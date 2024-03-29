# Проект cоциальная сеть YaTube API

**Описание**  

Позволяет публиковать, комментировать, удалять и редактировать посты, а также подписываться на понравившихся авторов с помощью API

**Технологии**

Python 3.7, Django 3.2, DRF, JWT, Joser

**Запуск проекта на локальной машине**

- Клонировать репозиторий
- Установите виртуальное окружение версия Python 3.7: ``` py -3.7 -m venv venv ```
- активируйте его ``` venv/Scripts/activate ```
- Затем нужно установить все зависимости из файла requirements.txt ``` pip install -r requirements.txt ```
- Выполняем миграции ``` python manage.py migrate ```
- Создаем суперпользователя: ``` python manage.py createsuperuser ```
- Запускаем проект: ``` python manage.py runserver ```

**Примеры работы с API для не авторизованных пользователей**

Не авторизованные пользователи могут работать с API только в режиме чтения

``` 
GET api/v1/posts/ - получить список всех публикаций.
GET api/v1/posts/{id}/ - получение публикации по id
GET api/v1/groups/ - получение списка всех групп
GET api/v1/groups/{id}/ - получение информации о группе по id
GET api/v1/{post_id}/comments/ - получение всех комментариев к посту
GET api/v1/{post_id}/comments/{id}/ - Получение комментария к посту по id
```

**Примеры работы с API для авторизованных пользователей**

Авторизованные пользователи могут подписываться, комментировать, удалять и редактировать посты

Создание поста:
```
POST /api/v1/posts/
```

Редактирование поста:
```
PUT /api/v1/posts/{id}/
```
