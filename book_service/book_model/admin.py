from django.contrib import admin

# Register your models here.
from book_model.models import book_model

admin.site.register(book_model)
