from django.apps import AppConfig


class CompanyConfig(AppConfig):
    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'company'
