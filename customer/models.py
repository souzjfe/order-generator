from django.db import models

class Customer(models.Model):
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['name']
    name = models.CharField(max_length=255, verbose_name='Nome')
    address = models.CharField(max_length=255, blank=True, verbose_name='Endereço')  
    phone = models.CharField(max_length=20, blank=True, verbose_name='Telefone')  
    cpf_cnpj = models.CharField(max_length=14, blank=True, verbose_name='CPF/CNPJ') 

    def __str__(self):
        return self.name