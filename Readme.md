# Тестирование Stripe

### Данный проект развернут по адресу [176.119.158.224](http://176.119.158.224), для входа в админку admin/admin. Сервер очень слабый (1 ядро/2.2ггц), потому прошу терпения,так как запросы могут долго выполняться.

### Для локального запуска и тестирования проекта вам потребуется Docker, аккаунт в сервисе Stripe с данными Publishable key и Secret key. Во время запуска проекта в базу будут загружены тестовые данные из `items_data.json`.

##### Выполните следующие команды:
1. Клонируйте репозиторий:
`git clone `
2. Перейдите в каталог Test-Stripe:
`cd Test-Stripe`
3. Создайте .env со следующими данными:
`SECRET_KEY=YOUR_DJANGO_SECRET_KEY`
`STRIPE_API_KEY=Publishable_key`
`STRIPE_PUBLIC_KEY=Secret key`
4. Запустите проект:
`sudo docker compose up -d --build`
5. Создайте суперпользователя:
`sudo docker compose exec backend python manage.py createsuperuser`
8. Проект будет доступен по адресу [http://localhost/](http://localhost/)

### В данном проекте вам доступны следующие эндпоинты:
- /items/ - Список достпуных итемов
- /item/id/ - Страница итема с возможностью покупки или добавления в корзину
