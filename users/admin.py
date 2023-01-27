from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreateForm, CustomUserChangeForm
# Register your models here.


class CustomUserAdmin (UserAdmin):
    add_form = CustomUserCreateForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['first_name', 'last_name',
                    'email', 'phone', 'is_staff', 'username']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais: ', {
         'fields': ('first_name', 'last_name', 'phone')}),
        ('Permissões: ', {'fields': ('is_active', 'is_staff',
         'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes: ', {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
