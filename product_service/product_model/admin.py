from django.contrib import admin

# Register your models here.
from product_model.models import product_details

admin.site.register(product_details)