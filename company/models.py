from django.db import models

class Company(models.Model):
    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ['cidade']
    cidade = models.CharField(max_length=255, verbose_name='Cidade')
    owner = models.CharField(max_length=255, verbose_name='Responsável (Nome que será apresentado no orçamento)')
    contact = models.CharField(max_length=255, verbose_name='Contato')
    address = models.TextField(verbose_name='Endereço')
    cnpj = models.CharField(max_length=18, unique=True, verbose_name='CNPJ')
    # user = models.ManyToManyField('auth.User', blank=True, verbose_name='Usuários')

    def __str__(self):
        return self.cidade
