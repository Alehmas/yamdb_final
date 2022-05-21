
## Описание

API для приложения Yatube разделенная на связанные контейнеры при помощи Docker Compose: контейнер с приложением, контейнер с базой данных, и контейнер со статикой

## Шаблон наполнения env-файла

Добавляем `.env` файл в папку `infra` и вносим необходимые данные.
Указываем, что :
- работаем с postgresql
`DB_ENGINE=django.db.backends.postgresql`
- имя базы данных
`DB_NAME=postgres`
- логин для подключения к базе данных
`POSTGRES_USER=admin`
- пароль для подключения к БД
`POSTGRES_PASSWORD=admin` 
- название сервиса (контейнера)
`DB_HOST=db`
- порт для подключения к БД
`DB_PORT=5432`

## Описание команд для запуска приложения в контейнерах:

Запустить docker compose:

`sudo docker compose up -d`

Выполните миграции:

`sudo docker compose exec web python manage.py migrate`

Создайте суперпользователя:

`sudo docker compose exec web python manage.py createsuperuser`

Скопируйте статистические файлы:

`sudo docker compose exec web python manage.py collectstatic --no-input`

## Описание команды для заполнения базы данными:

`http://localhost/api/v1/auth/signup/`  (POST) Регистрация нового пользователя

```
{
  "email": "string",
  "username": "string"
}

```

`http://localhost/api/v1/auth/token/`  (POST) Получение JWT-токена в обмен на username и confirmation code

```
{
  "username": "string",
  "confirmation_code": "string"
}

```

`http://localhost/api/v1/categories/`  (GET, POST, DELETE) Получение, добавление и удаление категорий (типов) произведений

```
{
  "name": "string",  
  "slug": "string"
}
```
