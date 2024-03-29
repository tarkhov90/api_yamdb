# Проект api_yamdb

### Используется:

[![Python](https://img.shields.io/badge/-Python_3.7.9-464646??style=flat-square&logo=Python)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/-Django-464646??style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django](https://img.shields.io/badge/-Django_rest_framework_3.12.4-464646??style=flat-square&logo=Django)](https://www.django-rest-framework.org)


## Описание
Проект YaMDb собирает отзывы (Review) пользователей на произведения (Titles). Произведения делятся на категории: «Книги», «Фильмы», «Музыка».
В каждой категории есть произведения: книги, фильмы или музыка. Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Насекомые» и вторая сюита Баха.
Произведению может быть присвоен жанр (Genre) из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). Новые жанры может создавать только администратор.
Пользователи оставляют к произведениям текстовые отзывы (Review) и ставят произведению оценку в диапазоне от одного до десяти 


#### Пользовательские роли
**Аноним** — может просматривать описания произведений, читать отзывы и комментарии.
**Аутентифицированный пользователь (user)** — может читать всё, как и Аноним, может публиковать отзывы и ставить оценки произведениям (фильмам/книгам/песенкам), может комментировать отзывы; может редактировать и удалять свои отзывы и комментарии, редактировать свои оценки произведений. Эта роль присваивается по умолчанию каждому новому пользователю.
**Модератор (moderator)** — те же права, что и у Аутентифицированного пользователя, плюс право удалять и редактировать любые отзывы и комментарии.
**Администратор (admin)** — полные права на управление всем контентом проекта. Может создавать и удалять произведения, категории и жанры. Может назначать роли пользователям.
**Суперюзер Django** должен всегда обладать правами администратора, пользователя с правами admin. Даже если изменить пользовательскую роль суперюзера — это не лишит его прав администратора. Суперюзер — всегда администратор, но администратор — не обязательно суперюзер.


# Ресурсы API YaMDb
**auth**: аутентификация.
**users**: пользователи.
**titles**: произведения, к которым пишут отзывы (определённый фильм, книга или песенка).
**categories**: категории (типы) произведений («Фильмы», «Книги», «Музыка»).
**genres**: жанры произведений. Одно произведение может быть привязано к нескольким жанрам.
**reviews**: отзывы на произведения. Отзыв привязан к определённому произведению.
**comments**: комментарии к отзывам. Комментарий привязан к определённому отзыву.


# Установка
Клонировать репозиторий и перейти в него в командной строке:
git clone https:
cd api_yamdb
Cоздать и активировать виртуальное окружение:

```
python -m venv env
```
```
source venv/scripts/activate
```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

## Авторы
- :white_check_mark: [Александр Фомичев](https://github.com/Fan160688)
- :white_check_mark: [Кирилл Чемизов](https://github.com/fingalropl)
- :white_check_mark: [Кирилл Тархов](https://github.com/Tarkhov90)

