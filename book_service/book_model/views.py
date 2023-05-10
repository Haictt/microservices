from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json

from django.views.decorators.csrf import csrf_exempt
from book_model.models import book_model

@csrf_exempt
def get_book_data(request):
    data = []
    resp = {}

    book_data = book_model.objects.all()

    for tbl_value in book_data.values():
        data.append(tbl_value)

    if data:
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['data'] = data
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Data is not available.'

    return HttpResponse(json.dumps(resp), content_type = 'application/json')

def data_insert(product_category, book_name, availability, price):
    book_data = book_model(
        product_category = product_category,
        book_name = book_name,
        availability = availability,
        price = price,
    )

    book_data.save()
    return 1

@csrf_exempt
# get the data from the front end.
def insertBook_req(request):
    product_category = request.POST.get("Product category")
    book_name = request.POST.get("Book name")
    availability = request.POST.get("Availability")
    price = request.POST.get("Price")
    resp = {}

    # checking that all fields are available.
    if product_category and book_name and availability and price :
        respdata = data_insert(product_category, book_name, availability, price)

        # if it returns value then will show success.
        if respdata:
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['message'] = 'Book is insert Successfully.'
        # else returning any value then the show will fail.
        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Unable insert book, Please try again.'
    # if any field is missing.
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'All fields are mandatory.'

    return HttpResponse(json.dumps(resp), content_type = "application/json")