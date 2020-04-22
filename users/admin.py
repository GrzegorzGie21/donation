from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User
from users.forms import ChangeUserForm, CreateUserForm


# Register your models here.
class MyUserAdmin(UserAdmin):
    add_form = CreateUserForm
    form = ChangeUserForm
    model = User
    list_display = ['email', 'is_staff', 'is_active']  # te pola wyświetlaja się na liście userów
    list_filter = ['email', 'city', 'is_staff', 'is_active']
    fieldsets = (
        (None, {'fields': ('email', 'password',), }),
        ('Personal info', {'fields': (('first_name', 'last_name'), 'city',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser',),
                         'classes': ('collapse',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active',)
        }),
    )
    search_field = 'email'
    ordering = ['email']


admin.site.register(User, MyUserAdmin)
