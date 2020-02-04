from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from django.views.generic import ListView
from invoice.models import Invoice


# Create your views here.
class InvoiceList(ListView):
    model = Invoice
    template_name = 'listinvoice.html'

