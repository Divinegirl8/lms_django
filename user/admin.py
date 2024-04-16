from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user.models import LibraryUser


# Register your models here.

@admin.register(LibraryUser)
class LibraryUserAdmin(UserAdmin):
    pass

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", 'first_name', 'last_name'),
            },
        ),
    )
