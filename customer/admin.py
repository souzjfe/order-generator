# admin.py
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django import forms
from customer.models import Customer
from django.contrib.admin.views.autocomplete import AutocompleteJsonView

class CustomerAutocomplete(AutocompleteJsonView):
    def get_queryset(self):
        return Customer.objects.all()
    
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'phone', 'number', 'neighborhood', 'street')
    fields = ('name', 'phone', 'cpf_cnpj', 'zip_code', 'number', 'neighborhood', 'street')
    
    class Media:
        js = (
            'js/fetch_address.js',  # Seu script personalizado, se houver
            'js/input_mask.js',  # Configurações de máscara inputmask
        )
