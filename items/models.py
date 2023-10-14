from django.db import models
from stores.models import Store
# Create your models here.


class ItemCategory(models.Model):
    name = models.CharField(max_length=255)
    store = models.ForeignKey(to=Store,on_delete=models.CASCADE)

class Item(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255,blank=True)
    description = models.TextField( blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=0)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    quantity = models.IntegerField(default=0)
    image_link = models.CharField(max_length=255,blank=True)
    store = models.ForeignKey(to=Store,on_delete=models.CASCADE)
    category = models.ForeignKey(to=ItemCategory,on_delete=models.CASCADE)
