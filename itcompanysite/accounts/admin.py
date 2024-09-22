from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import StudentCreationForm
from .models import *

User = get_user_model()

@admin.register(User)
class UserAdmin(UserAdmin):
    # Поля, которые будут отображаться в списке пользователей
    list_display = ('email', 'username', 'role', 'is_active', 'is_staff', 'email_verify')

    # Поля, которые можно редактировать при создании/редактировании пользователя
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),  # Добавляем поле 'role'
    )
    add_form = StudentCreationForm
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "password1", "password2"),
            },
        ),
    )


admin.register(File)
admin.register(UserFiles)
