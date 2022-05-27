from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=123)
    author = models.CharField(max_length=123)
    price = models.CharField(max_length=123)
    summery = models.TextField()
    image = models.ImageField(upload_to='Book/')
    is_favorite = models.ForeignKey('User.UserFavorite', on_delete=models.SET_NULL, null=True, blank=True)
    category_id = models.ForeignKey('Category.Category', on_delete=models.SET_NULL, null=True, blank=True)
    creator = models.ForeignKey('User.User', on_delete=models.SET_NULL, null=True, blank=True)
    create_Date = models.DateTimeField(auto_now_add=True)
