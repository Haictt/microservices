from __future__ import unicode_literals
from django.db import models

class book_model(models.Model):
    book_id = models.CharField(max_length=10)
    product_category = models.CharField(max_length=50)
    book_name = models.CharField(max_length=100)
    availability = models.CharField(max_length=15)
    price = models.CharField(max_length=10)

    def __str__(self):
        return '%s %s %s %s %s' % (self.book_id, self.product_category, self.book_name, self.availability, self.price)