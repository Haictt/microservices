from __future__ import unicode_literals
from django.db import models

class shoe_model(models.Model):
    shoe_id = models.CharField(max_length=10)
    product_category = models.CharField(max_length=50)
    shoe_name = models.CharField(max_length=100)
    availability = models.CharField(max_length=15)
    price = models.CharField(max_length=10)
    color = models.CharField(max_length=10)
    size = models.CharField(max_length=10)
    def __str__(self):
        return '%s %s %s %s %s %s %s' % (self.shoe_id, self.product_category, self.shoe_name, self.availability, self.price,self.color,self.size)