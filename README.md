# Where-to-go
 
Сайт, на котором показаны достопримечательности Москвы.

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```powershell
pip install -r requirements.txt
```
### Настройка переменных окружений

Чтобы настроить переменные окружения нужно создать файл с названием `.env` и настраивать. Вот какие есть переменные окружения:
1. `ALLOWED_HOSTS` - домены, под которыми можно запускать сайт. По умолчанию: `['127.0.0.1', '.pythonanywhere.com']`.
2. `SECRET_KEY` - секретный ключ приложения.
3. `DEBUG` - режим отладки. По умолчанию: `False`.
Вот пример файла `.env`:
```
DEBUG=True
ALLOWED_HOSTS=[]
SECRET_KEY='REPLACE_ME'
```

### Как запустить
Перед запуском сайта нужно создать базу данных и применить к ней миграции. Это можно сделать командой:
```powershell
python3 manage.py migrate
```

Теперь можно запустить код с помощью команды:
```powershell
python3 managr.py runserver
```

### Использование админ панели

Для начала, нужно создать аккаунт суперпользователя. Это можно сделать командой:
```powershell
python3 manage.py createsuperuser
```
Теперь можно перейти по ссылке `/admin` и войти под логином и паролем, который Вы указали при регистрации.

### Загрузка данных в базу данных

Для загрузки данных в базу данных можно использовать команду:
```
python3 manage.py load_place https://ссылка_на_json_файл
```
Вот пример json файла:
```
{
    "title": "Экскурсионная компания «Легенды Москвы»",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/4f793576c79c1cbe68b73800ae06f06f.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/7a7631bab8af3e340993a6fb1ded3e73.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/a55cbc706d764c1764dfccf832d50541.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/65153b5c595345713f812d1329457b54.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/0a79676b3d5e3b394717b4bf2e610a57.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/1e27f507cb72e76b604adbe5e7b5f315.jpg"
    ],
    "description_short": "Неважно, живёте ли вы в Москве всю жизнь или впервые оказались в столице, составить ёмкий, познавательный и впечатляющий маршрут по городу — творческая и непростая задача. И её с удовольствием берёт на себя экскурсионная компания «Легенды Москвы»!",
    "description_long": "<p>Экскурсия от компании «Легенды Москвы» — простой, удобный и приятный способ познакомиться с городом или освежить свои чувства к нему. Что выберете вы — классическую или необычную экскурсию, пешую прогулку или путешествие по городу на автобусе? Любые варианты можно скомбинировать в уникальный маршрут и создать собственную индивидуальную экскурсионную программу.</p><p>Компания «Легенды Москвы» сотрудничает с аккредитованными экскурсоводами и тщательно следит за качеством экскурсий и сервиса. Автобусные экскурсии проводятся на комфортабельном современном транспорте. Для вашего удобства вы можете заранее забронировать конкретное место в автобусе — это делает посадку организованной и понятной.</p><p>По любым вопросам вы можете круглосуточно обратиться по телефонам горячей линии.</p><p>Подробности узнавайте <a class=\"external-link\" href=\"https://moscowlegends.ru \" target=\"_blank\">на сайте</a>. За обновлениями удобно следить <a class=\"external-link\" href=\"https://vk.com/legends_of_moscow \" target=\"_blank\">«ВКонтакте»</a>, <a class=\"external-link\" href=\"https://www.facebook.com/legendsofmoscow?ref=bookmarks \" target=\"_blank\">в Facebook</a>.</p>",
    "coordinates": {
        "lng": "37.64912239999976",
        "lat": "55.77754550000014"
    }
}
```
### Сайт

Как выглядит сайт можно посмотреть по [по ссылке](https://olberd.pythonanywhere.com/)

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).