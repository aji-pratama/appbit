from __future__ import unicode_literals

from decimal import Decimal
from django.db import models

class Category(models.Model):
    title = models.CharField(blank=True, max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    name     = models.CharField(blank=True, max_length=100)
    photo    = models.CharField(blank=True, max_length=100)
    model    = models.CharField(blank=False, max_length=100)
    price    = models.DecimalField(max_digits=20,decimal_places=2,default=Decimal('0.00'))

    def __str__(self):
        return self.name

class CategoryProduct(models.Model):
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.product
