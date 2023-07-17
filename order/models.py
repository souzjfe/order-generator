from django.db import models
from customer.models import Customer
from product.models import Product

class Order(models.Model):
    class Meta:
        verbose_name = 'Orçamento'
        verbose_name_plural = 'Orçamentos'
        ordering = ['-created_at']
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Cliente')
    leased_equipment = models.BooleanField(verbose_name='Equipamento alugado')
    monthly_fee = models.DecimalField(blank=True, max_digits=10, decimal_places=2, verbose_name='Valor mensalidade')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de emissão')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de atualização')
    verbose_name = 'Orçamento'
    def __str__(self):
        return f"Orçamento #{self.pk} - {self.customer.name}"


class OrderItem(models.Model):
    class Meta:
        verbose_name = 'Item do orçamento'
        verbose_name_plural = 'Itens do orçamento'
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Orçamento')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Produto')
    quantity = models.PositiveIntegerField(verbose_name='Quantidade')

    def __str__(self):
        return f"Orçamento #{self.order.pk} - {self.product.name}"
