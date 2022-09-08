from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
<<<<<<< HEAD

from .validators import year_validator
=======
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

>>>>>>> 6434cef6116010490d83dcc8f5fb5355338041ca

User = get_user_model()
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

class GenreTitle(models.Model):
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    title = models.ForeignKey('Title', on_delete=models.CASCADE)

class Review(models.Model):
    """Модель отзывов"""
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews')
    score = models.IntegerField(
        validators=[
            MinValueValidator(1, 'Минимальный рейтинг 1'),
            MaxValueValidator(10, 'Максимальный рейтинг 10')]
    )
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE,
        related_name="reviews", null=True
    )

    def __str__(self):
        return self.text


class Comment(models.Model):
    """Модель комментариев"""
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)