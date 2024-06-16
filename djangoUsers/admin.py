from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from djangoUsers.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            'Custom fields',
            {
                'fields': (
                    'phone',
                    'status',
                    'birth_date',
                    'city',
                    'subscribe'
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
                    'phone',
                    'status',
                    'birth_date',
                    'city',
                    'subscribe'
                )
            }
        )
    )