from django.contrib import admin
from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
  list_display = ('cidade', 'contact', 'cnpj')
  search_fields = ('cidade', 'cnpj')
    
    
  class Media:
    js = (
      'js/input_mask_company.js',  # Configurações de máscara inputmask
    )