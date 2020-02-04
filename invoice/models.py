from django.db import models

# Create your models here.
class Invoice(models.Model):
    receiver_name = models.CharField(max_length=30)
    receiver_address = models.CharField(max_length=100)
    invoice_no = models.AutoField(primary_key=True)
    invoice_date = models.DateTimeField()
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    actual_amount = models.DecimalField(max_digits=9,decimal_places=2)
    other_amount = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    total = models.DecimalField(max_digits=9,decimal_places=2)

    def actual_amount(self):
        return self.quantity * self.price
    def total(self):
        return self.quantity * self.price + self.other_amount
    def __str__(self):
        return self.receiver_name


