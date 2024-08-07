"""
URL configuration for ordergenerator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from order.views import GeneratePDF
from product.admin import ProductAutocomplete
from customer.admin import CustomerAutocomplete

urlpatterns = [
    path('order/<int:order_id>/pdf/', GeneratePDF.as_view(), name='generate_pdf'),
    path("", admin.site.urls),
    path('auto/product/', ProductAutocomplete.as_view(), name='product-autocomplete'),
    path('auto/customer/', CustomerAutocomplete.as_view(), name='customer-autocomplete'),
]
