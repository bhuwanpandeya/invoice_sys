from django.contrib import admin
from .models import Invoice

# Register your models here.

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_no', 'receiver_name', 'receiver_address','invoice_date','item_name','quantity','price', 'actual_amount','other_amount', 'total')
admin.site.register(Invoice, InvoiceAdmin)
