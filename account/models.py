from django.contrib.auth.models import AbstractUser
from django.db import models
from company.models import Company

class CustomUser(AbstractUser):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.username
