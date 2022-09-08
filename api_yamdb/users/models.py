from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    ROLES = (
        ('user', 'User'),
        ('moderator', 'Moderator'),
        ('admin', 'Admin'),
    )
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[\w.@+-]+',
                message=('Required. 150 characters or fewer. '
                         'Letters, digits and @/./+/-/_ only.')
            )
        ]
    )
    password = models.CharField(
        max_length=100,
        blank=True,
    )
    email = models.EmailField(
        max_length=254,
        unique=True,
    )
    first_name = models.CharField(
        max_length=150,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=150,
        blank=True,
        null=True,
    )
    role = models.CharField(
        max_length=20,
        choices=ROLES,
        default='user',
    )
    bio = models.TextField(
        max_length=500,
        blank=True,
    )

    @property
    def is_admin(self):
        return self.role == 'admin'

    @property
    def is_moderator(self):
        return self.role == 'moderator'