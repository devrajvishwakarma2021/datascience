

# Create your models here.
from statistics import quantiles
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=220)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.name)

class Purchase(models.Model):        
    product =models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.PositiveBigIntegerField()
    quantity =models.PositiveBigIntegerField()
    total_price = models.PositiveBigIntegerField(blank=True)
    salesman =models.ForeignKey(User, on_delete=models.CASCADE)

    date =   models.DateTimeField(default=timezone.now)
    # (auto_now_add=True)

    def save (self, *args, **kwargs):
          self.total_price =self.price * self.quantity
          super().save(*args, **kwargs)

    def __str__(self):
         return "solled {} - {} for {}".format(self.product.name, self.quantity, self.price)


