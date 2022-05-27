from django.contrib import admin
from Category.models import Category


class AdminCategory(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        obj.creator = request.user.id
        return super().save_model(request, obj, form, change)


admin.site.register(Category, AdminCategory)
