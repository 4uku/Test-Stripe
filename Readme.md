# Тестирование Stripe

### Данная работа развернута по адресу []() с использованием Docker, docker-compose и nginx. Подробнее можно посмотреть в ветке develop.

### Для локального запуска и тестирования работы вам потребуется Docker. Выполните следующие команды:
1. Клонируйте репозиторий:
`git clone `
2. Соберите образ из докерфайла:
`sudo docker build -t test-stripe .`
3. Запустите контейнер на основе образа:
`sudo docker run -d --name test-stripe -it -p 8000:8000 test-stripe`
4. Примените миграции:
`sudo docker container exec -it test-stripe python manage.py migrate`
5. Загрузите тестовые данные в базу:
`sudo docker container exec -it test-stripe python manage.py upload_items`
6. Создайте суперпользователя:
`sudo docker container exec -it test-stripe python manage.py createsuperuser`
7. Соберите статику:
`sudo docker container exec -it test-stripe python manage.py collectstatic`
8. Проект будет доступен по адресу [http://localhost:8000/](http://localhost:8000/)

### В данной работе вам доступны следующие эндпоинты:
- /items/ - Список достпуных итемов
- /item/id/ - Страница итема с возможностью покупки или добавления в корзину
