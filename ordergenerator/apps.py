from django.contrib.admin.apps import AdminConfig

class AdminConfigReorder(AdminConfig):
    default_site = 'ordergenerator.admin.AdminSiteReorder'