from __future__ import unicode_literals
from django.db import models

class clothe_model(models.Model):
    clothe_id = models.CharField(max_length=10)
    product_category = models.CharField(max_length=50)
    clothe_name = models.CharField(max_length=100)
    availability = models.CharField(max_length=15)
    price = models.CharField(max_length=10)
    color = models.CharField(max_length=10)
    def __str__(self):
        return '%s %s %s %s %s %s' % (self.clothe_id, self.product_category, self.clothe_name, self.availability, self.price,self.color)