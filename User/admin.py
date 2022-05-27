from django.contrib import admin

from User.models import UserFavorite, User


class AdminUser(admin.ModelAdmin):
    pass


class AdminUserFavorite(admin.ModelAdmin):
    pass


admin.site.register(User, AdminUser)
admin.site.register(UserFavorite, AdminUserFavorite)
