from django.contrib import admin

from customer.models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'cpf_cnpj')
    fields = ('name', 'address', 'phone', 'cpf_cnpj')