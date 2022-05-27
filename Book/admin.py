from django.contrib import admin

from Book.models import Book


class AdminBook(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        obj.creator = request.user.id
        return super().save_model(request, obj, form, change)


admin.site.register(Book, AdminBook)
