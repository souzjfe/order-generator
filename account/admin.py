# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form_template = 'admin/auth/user/add_form.html'
    
    # Campos a serem exibidos na visualização de detalhes do usuário
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('company',)}),
    )
    
    # Campos a serem exibidos no formulário de criação do usuário
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('company',)}),
    )
    
    # Definir o modelo de formulário para adicionar e alterar usuários
    form = UserAdmin.form
    add_form = UserAdmin.add_form
    
    list_display = ['username', 'email', 'first_name', 'last_name', 'company']
    list_filter = ['is_staff', 'is_superuser', 'is_active', 'company']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    ordering = ['username']

admin.site.register(CustomUser, CustomUserAdmin)
