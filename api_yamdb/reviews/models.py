from django.contrib.auth import get_user_model
from django.db import models
from django.core.exceptions import MinValueValidator, MaxValueValidator

User = get_user_model()


class Title(models.Model):
    None


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
