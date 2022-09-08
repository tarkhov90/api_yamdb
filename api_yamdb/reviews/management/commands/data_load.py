from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import csv
from csv import DictReader
import os
from reviews.models import Review, Comment


# class Command(BaseCommand):

#     def handle(self, *args, **options):
#         with open(os.join.path(settings.BASE_DIR / 'review.csv'), 'r') as csv_file:
#             csv_reader = csv.reader(csv_file, delimiter=';')
#             for row in csv_reader:
#                 Review.objects.create(name=row[2], description=row[3], price=row[4])

ALREDY_LOADED_ERROR_MESSAGE = """
Если вам нужно перезагрузить дочерние данные из CSV-файла,
сначала удалите файл db.sqlite3, чтобы уничтожить базу данных.
Затем запустите `python manage.py миграция` для новой пустой
базы данных с таблицами"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Загрузка данных из файла review.csv"

    def handle(self, *args, **options):
        # Текст, если данные уже существуют в БД
        if Review.objects.exists():
            print('дочерние данные уже загружены...существуют.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return
        
        # Текст перед загрузкой данных в БД
        print("Загрузка данных ")

        #Код для загрузки данных в БД
        for row in DictReader(open(f"{settings.BASE_DIR}/static/data/{'review.csv'}", encoding='utf-8')):
            review = Review(text=row['text'], pub_date=row['pub_date'], author=row['author'],
                            score=row['score'])
            review.save()

        # for row in DictReader(open(f"{settings.BASE_DIR}/static/data/{'comments.csv'}", encoding='utf-8')):
        #     comment = Comment(text=row['text'], pub_date=row['pub_date'], author=row['author'],
        #                         review_id=row['review_id'])
        #     comment.save()
