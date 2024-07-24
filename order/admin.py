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
    autocomplete_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    
    list_display = ('customer', 'created_at', 'updated_at', 'download_pdf', 'whatsapp_button')
    fields = ('customer', 'monthly_fee', 'maximum_installments', 'cash_discount_percentage', )
    inlines = [OrderItemInline]
    actions = ['generete_pdf']
    autocomplete_fields = ['customer']
    

    def download_pdf(self, obj):
        return format_html('<a class="button" href="/order/{}/pdf/">Baixar PDF</a>', obj.pk)
    download_pdf.short_description = 'PDF'

    def generete_pdf(self, request, queryset):
        for order in queryset:
            reverse('/order/{}/pdf/'.format(order.pk))
            
    generete_pdf.short_description = 'Baixar selecionados em PDF'
    # def send_via_whatsapp(self, request, queryset):
    #     # Lógica para enviar via WhatsApp
    #     for order in queryset:
    #         whatsapp_url = 'https://api.whatsapp.com/send?phone=SEUNUMERO&text=' + urllib.parse.quote(f"Olá, segue o PDF do pedido {order.pk}: {request.build_absolute_uri(reverse('nome_da_view_do_pdf', args=[order.pk]))}")
    #         return format_html('<a class="button" href="{}" target="_blank">Enviar via WhatsApp</a>', whatsapp_url)
    
    # send_via_whatsapp.short_description = 'Enviar via WhatsApp'

    def whatsapp_button(self, obj):
        if obj.customer.phone:
            phone = obj.customer.phone
            pdf_url = f'/order/{obj.pk}/pdf/'  # Substitua pela sua URL real de download do PDF
            message = f'Olá, estou interessado no pedido #{obj.pk}. Aqui está o link para o PDF: {pdf_url}'
            url = f'https://api.whatsapp.com/send?phone={phone}&text={message}'
            return format_html('<a class="button" target="_blank" href="{}">Iniciar WhatsApp</a>', url)
        return '-'
    whatsapp_button.short_description = 'WhatsApp'
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
