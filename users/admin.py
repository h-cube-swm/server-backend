from django.contrib import admin
from .models import User

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "uid", "user_type")


admin.site.register(User, UserAdmin)
