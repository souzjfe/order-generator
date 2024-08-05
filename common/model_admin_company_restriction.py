from django.contrib import admin
from django.db import models

class ModelAdminCompanyRestriction(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not obj.company:
            obj.company = request.user.company
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        company = request.user.company
        return qs.filter(models.Q(company=company) | models.Q(company__isnull=True))

    
