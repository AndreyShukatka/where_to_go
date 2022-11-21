# Куда пойти — Москва глазами Артёма

Авторский проект Артёма.

![&#x41A;&#x443;&#x434;&#x430; &#x43F;&#x43E;&#x439;&#x442;&#x438;](https://github.com/MaksAnikeev/where_to_go/blob/main/.gitbook/assets/site.png)

[Пример работы сайта](http://slon1k.pythonanywhere.com).

## Запуск

Для запуска сайта вам понадобится Python 3.

Скачайте код с GitHub. Установите зависимости:

```
pip install -r requirements.txt
```

### Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 3 переменные:
- `DEBUG` — дебаг-режим. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта
- `ALLOWED_HOSTS` — см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts),
  при развертывании сайта на `pythonanywhere` здесь нужно указать `ALLOWED_HOSTS='......pythonanywhere.com'`

Создайте базу данных SQLite

```
python manage.py migrate
```

Соберите все файлы статики в одном месте. Создайте в корневом каталоге папку `static`

И запустите сервер с командой `collectstatic`
```
python manage.py collectstatic
```

Запустите сервер

```
python manage.py runserver
```

## Настройки

Внизу справа на странице можно включить отладочный режим логгирования.

![debug mode](https://github.com/MaksAnikeev/where_to_go/blob/main/.gitbook/assets/debug-option.png)

Настройки сохраняются в Local Storage браузера и не пропадают после обновления страницы. Чтобы сбросить настройки удалите ключи из Local Storage с помощью Chrome Dev Tools —&gt; Вкладка Application —&gt; Local Storage.


## Занесение данных через панель администратора

Чтобы использовать админ панель создайте суперпользователя

```
python manage.py createsuperuser
```
Панель администратора будет находится по адресу:

`http://127.0.0.1:8000/admin/`

Либо, если вы смотрите пример работы админки сайта:

`http://slon1k.pythonanywhere.com/admin`

Текущее имя - `admin`, пароль - `admin`

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).
