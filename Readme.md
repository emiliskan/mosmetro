# News API

Реализоция API для получения последних новостей с [mosmetro.ru/news ]()

С помощью `Celery` данные периодически загружаются в `Mongo`, а api
построенное на `flask` открывает ручку для получения последних новостей

# Запуск
`docker compose up --build`

# data_loader

Здесь скрипты для парсинга новостей с сайта и загрузки в базу.
Периодический их запуск обеспечивается с помощью `Celery`.

### Сделать бы еще:
- Возможно стоит сделать абстракцию для парсинга, хотя текущая
реализация позволяет подключать парсеры кастомные
- Попытаться объединить celery worker и beat в один инстанс,
не получилось сделать это сразу
- Проверить не будет ли ошибок из-за timezone

# news_api

Приложение на `flask`, открывающая ручку для поулчения новостей
с фильтрацией по количеству дней, смещению и лимиту.

### Сделать бы еще:
- Валидация входящих параметров, например, чтоб limit не
был выше определенного значения
- Перенести код ручки в отдельный файл
- Кажется оверхедом как сейчас происходит сбор и возврат результата из базы,
стоит посмотреть в сторону [FlaskPydanticSpec](https://github.com/turner-townsend/flask-pydantic-spec)
- Сделать сервис получения новостей классом
- Работу с базой сделать абстрактной, для подключение других бд

# Почему `MongoDB`:
- Нет необходимости в связях с другими таблицами
- Легкое горизонтальное мастштабирование