from django.db import models

class Product(models.Model):
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['name']
    name = models.CharField(max_length=255, verbose_name='Nome')
    description = models.TextField(blank=True, verbose_name='Descrição')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço unitário')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de atualização')
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Empresa')


    def __str__(self):
        return self.name

