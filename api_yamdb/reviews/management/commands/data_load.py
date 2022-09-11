from django.core.management.base import BaseCommand
from django.conf import settings
from csv import DictReader

from reviews.models import Review
from users.models import User


ALREDY_LOADED_ERROR_MESSAGE = """
Если вам нужно перезагрузить дочерние данные из CSV-файла,
сначала удалите файл db.sqlite3, чтобы уничтожить базу данных.
Затем запустите `python manage.py миграция` для новой пустой
базы данных с таблицами"""


class Command(BaseCommand):
    help = "Загрузка данных из файла review.csv"

    def handle(self, *args, **options):
        if Review.objects.exists():
            print('дочерние данные уже загружены...существуют.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return
        print("Загрузка данных ")
        for row in DictReader(open(
                f"{settings.BASE_DIR}/static/data/{'review.csv'}",
                encoding='utf-8')):
            review = Review(text=row['text'], pub_date=row['pub_date'],
                            author=User.objects.get(id=row['author']),
                            score=row['score'])
            review.save()
