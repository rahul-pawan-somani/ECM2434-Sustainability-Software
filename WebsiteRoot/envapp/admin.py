from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserTable

class CustomUserAdmin(UserAdmin):
    model = UserTable
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )

admin.site.register(UserTable, CustomUserAdmin)