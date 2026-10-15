"""
URL configuration for factor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from django.urls import path
from .views import HomeView
from django.urls import path
from .views import (
    InvoiceListView,
    InvoiceDetailView,
    InvoiceCreateView,
    InvoiceUpdateView,
    InvoiceDeleteView,
)

app_name = "home"
urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
    path("invoices/", InvoiceListView.as_view(), name="invoice_list"),
    path("invoice/<int:pk>/", InvoiceDetailView.as_view(), name="invoice_detail"),
    path("invoice/new/", InvoiceCreateView.as_view(), name="invoice_create"),
    path("invoice/<int:pk>/edit/", InvoiceUpdateView.as_view(), name="invoice_update"),
    path(
        "invoice/<int:pk>/delete/", InvoiceDeleteView.as_view(), name="invoice_delete"
    ),
]
