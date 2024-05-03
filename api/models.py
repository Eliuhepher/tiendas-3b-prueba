from django.db import models
from .model_settings import Constants
import uuid
 
class Product(models.Model):
    sku = models.CharField(max_length=50, primary_key=True, null=False)
    name = models.CharField(max_length=100, blank=False)
    stock = models.PositiveBigIntegerField(null=True, default=Constants.DEFAULT_QUANTITY_ON_INSERT.value)

    def __str__(self) -> str:
        return self.sku + "|" + self.name
    
class Order(models.Model):
    id = models.UUIDField(primary_key=True,  default=uuid.uuid4, editable=False)
    total = models.PositiveBigIntegerField()
    sales_channel = models.CharField(max_length=50, null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    