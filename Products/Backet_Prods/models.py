from django.db import models
from django.conf import settings
from SuperProds.models import Product


class Basket(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    

class BasketItem(models.Model):
    basket = models.ForeignKey(Basket, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    