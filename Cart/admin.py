from django.contrib import admin
from Cart.models import Cart


class AdminCart(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        obj.creator = request.user.id
        return super().save_model(request, obj, form, change)


admin.site.register(Cart, AdminCart)
