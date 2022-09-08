from django.db import models

from .validators import year_validator


class Category(models.Model):
    name = models.CharField(max_length=256, verbose_name='Категория')
    slug = models.SlugField(unique=True, verbose_name='Слаг категорий',
                            max_length=50)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(verbose_name='Жанр', max_length=50)
    slug = models.SlugField(unique=True, verbose_name='Слаг жанра')

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.name


class Title(models.Model):
    category = models.ForeignKey(Category,
                                 verbose_name='Категория произведения',
                                 on_delete=models.SET_NULL, null=True)
    genre = models.ManyToManyField(Genre,
                                   verbose_name='Жанр произведения')
    name = models.CharField(verbose_name='Название произведения',
                            max_length=256)
    year = models.IntegerField(validators=(year_validator,),
                               verbose_name='Год выпуска произведения')
    description = models.CharField(verbose_name='Описание', max_length=256)

    class Meta:
        verbose_name = "Произведение"
        verbose_name_plural = "Произведения"

    def __str__(self):
        return self.name

