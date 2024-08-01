from django.db import models

class Customer(models.Model):
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['name']
    name = models.CharField(max_length=255, verbose_name='Nome')
    street = models.CharField(max_length=255, blank=True, verbose_name='Rua')  
    number = models.IntegerField(blank=True, verbose_name='Número', default=0)
    zip_code = models.CharField(max_length=9, blank=True, verbose_name='CEP')
    neighborhood = models.CharField(max_length=255, blank=True, verbose_name='Bairro')
    phone = models.CharField(max_length=15, blank=True, verbose_name='Telefone')  
    cpf_cnpj = models.CharField(max_length=18, blank=True, verbose_name='CPF/CNPJ') 
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Empresa')

    def __str__(self):
        return self.name