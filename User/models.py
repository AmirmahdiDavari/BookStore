from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    roles = ((1, 'admin'), (2, 'owner'), (3, 'user'))
    phone_number = models.CharField(max_length=123, null=True, blank=True)
    role = models.IntegerField(choices=roles, default=1)


class UserFavorite(models.Model):
    book_id = models.ForeignKey('Book.Book', on_delete=models.SET_NULL, null=True, blank=True)
    user_id = models.ForeignKey('User.User', on_delete=models.SET_NULL, null=True, blank=True)
