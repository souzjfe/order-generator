# admin.py
from django.contrib import admin
from customer.models import Customer
from django.contrib.admin.views.autocomplete import AutocompleteJsonView
import common

class CustomerAutocomplete(AutocompleteJsonView):
    def get_queryset(self):
        return Customer.objects.all()
    
@admin.register(Customer)
class CustomerAdmin(common.ModelAdminCompanyRestriction):
    search_fields = ['name']
    list_display = ('name', 'phone', 'number', 'neighborhood', 'street')
    fields = ('name', 'phone', 'cpf_cnpj', 'zip_code', 'number', 'neighborhood', 'street')
    
    class Media:
        js = (
            'js/fetch_address.js',  # Seu script personalizado, se houver
            'js/input_mask_customer.js',  # Configurações de máscara inputmask
        )
