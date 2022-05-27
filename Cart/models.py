from django.db import models


class Cart(models.Model):
    book_id = models.ForeignKey('Book.Book', on_delete=models.SET_NULL, null=True, blank=True)
    discuont_code = models.CharField(max_length=123)
    discuonted_price = models.CharField(max_length=123)
    creator = models.ForeignKey('User.User', on_delete=models.SET_NULL, null=True, blank=True)
    create_Date = models.DateTimeField(auto_now_add=True)
