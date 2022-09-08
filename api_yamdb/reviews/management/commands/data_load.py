from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import csv
import os
from reviews.models import Category, Comment, Genre, Review, Title, User


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open(os.join.path(settings.BASE_DIR / 'review.csv'), 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            for row in csv_reader:
                Review.objects.create(name=row[2], description=row[3], price=row[4])

