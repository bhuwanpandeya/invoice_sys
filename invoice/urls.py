from django.urls import path
from . import views
from invoice.views import InvoiceList
from django.views.generic import TemplateView



urlpatterns = [
    path('', InvoiceList.as_view(), name='listinvoice'),
    path('create/', TemplateView.as_view(template_name="createinvoice.html")),
]
