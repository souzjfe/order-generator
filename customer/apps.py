from django.apps import AppConfig


class CustomerConfig(AppConfig):
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
    default_auto_field = "django.db.models.BigAutoField"
    name = "customer"
