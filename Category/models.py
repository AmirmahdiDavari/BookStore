from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=123)
    weight = models.IntegerField()
    creator = models.ForeignKey('User.User', on_delete=models.SET_NULL, null=True, blank=True)
    create_Date = models.DateTimeField(auto_now_add=True)
