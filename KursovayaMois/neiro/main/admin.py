from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'fio', 'email', 'gender', 'birth_date', 'image', 'bit']
    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            'Custom fields',
            {
                'fields': (
                    'fio',
                    'gender',
                    'birth_date',
                    'image',
                )
            }
        )
    )
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Custom fields',
            {
                'fields': (
                    'fio',
                    'gender',
                    'birth_date',
                    'image',
                )
            }
        )
    )
