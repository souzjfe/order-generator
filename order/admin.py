from django import forms
from django.contrib import admin
from django.shortcuts import redirect
from django.utils.html import format_html
from product.models import Product
from .models import Order, OrderItem
from django.urls import reverse

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    
    list_display = ('customer', 'created_at', 'updated_at', 'download_pdf' )
    fields = ('customer', 'leased_equipment', 'monthly_fee')
    inlines = [OrderItemInline]
    actions = ['generete_pdf']
    

    def download_pdf(self, obj):
        return format_html('<a class="button" href="/order/{}/pdf/">Baixar PDF</a>', obj.pk)
    download_pdf.short_description = 'PDF'

    def generete_pdf(self, request, queryset):
        for order in queryset:
            reverse('/order/{}/pdf/'.format(order.pk))
            
    generete_pdf.short_description = 'Baixar selecionados em PDF'

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if not change:
            products = form.cleaned_data.get('products')
            for product in products:
                OrderItem.objects.create(order=obj, product=product)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['products'] = forms.ModelMultipleChoiceField(
            queryset=Product.objects.all(),
            required=False
        )
        return form
