# product/admin.py
from django.urls import path
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django import forms
from django.contrib import admin

import common.model_admin_company_restriction
from .models import Product
import pandas as pd
from django.contrib.admin.views.autocomplete import AutocompleteJsonView
from django.db import models
import common
class ProductAutocomplete(AutocompleteJsonView):
    def get_queryset(self):
        return Product.objects.all()

class ProductImportForm(forms.Form):
    file = forms.FileField(label="Selecione a planilha no formato XLSX")

@admin.register(Product)
class ProductAdmin(common.model_admin_company_restriction.ModelAdminCompanyRestriction):
    search_fields = ['name']
    list_display = ('name', 'price', 'created_at', 'updated_at')
    fields = ('name', 'description', 'price')

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('import-products/', self.admin_site.admin_view(self.import_products), name='import_products'),
            path('export-products/', self.admin_site.admin_view(self.export_products), name='export_products'),
        ]
        return custom_urls + urls

    def export_products(self, request):
        company = request.user.company
        products = Product.objects.filter(models.Q(company=company) | models.Q(company__isnull=True))
        data = {
            'Código Produto': [product.pk for product in products],
            'Descrição do Produto': [product.name for product in products],
            'Preço Unitário': [product.price for product in products],
        }
        df = pd.DataFrame(data)
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=produtos.xlsx'
        with pd.ExcelWriter(response, engine='openpyxl') as writer:
            df.to_excel(writer, index=False)
        return response
    
    def import_products(self, request):
        if request.method == "POST":
            form = ProductImportForm(request.POST, request.FILES)
            if form.is_valid():
                file = form.cleaned_data['file']
                self.handle_import(file, request.user)
                messages.success(request, "Produtos importados com sucesso!")
                return redirect('..')
        else:
            form = ProductImportForm()

        return render(request, 'admin/import_products.html', {'form': form})

    def handle_import(self, file, user):
        company = user.company
        df = pd.read_excel(file)
        for index, row in df.iterrows():
            description = row['Descrição do Produto']
            price = row['Preço Unitário']
            Product.objects.update_or_create(
                name=description,
                defaults={'price': price, 'company': company}
            )

    def save_model(self, request, obj, form, change):
        if not obj.company:
            obj.company = request.user.company
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        company = request.user.company
        return qs.filter(models.Q(company=company) | models.Q(company__isnull=True))

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['custom_button_import'] = 'import-products/'
        extra_context['custom_button_export'] = 'export-products/'
        return super(ProductAdmin, self).changelist_view(request, extra_context=extra_context)
