from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json

from django.views.decorators.csrf import csrf_exempt
from shoe_model.models import shoe_model

@csrf_exempt
def get_shoes(request):
    data = []
    resp = {}

    prod_data = shoe_model.objects.all()

    for tbl_value in prod_data.values():
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

def data_insert(product_category, shoe_name, availability, price,color,size):
    shoe_data = shoe_model(
        product_category = product_category,
        shoe_name = shoe_name,
        availability = availability,
        price = price,
        color = color,
        size = size
    )

    shoe_data.save()
    return 1

@csrf_exempt
# get the data from the front end.
def insertShoe_req(request):
    product_category = request.POST.get("Product category")
    shoe_name = request.POST.get("Shoe name")
    availability = request.POST.get("Availability")
    price = request.POST.get("Price")
    color = request.POST.get("Color")
    size = request.POST.get("Size")
    resp = {}

    # checking that all fields are available.
    if product_category and shoe_name and availability and price and color and size:
        respdata = data_insert(product_category, shoe_name, availability, price,color,size)

        # if it returns value then will show success.
        if respdata:
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['message'] = 'Shoe is insert Successfully.'
        # else returning any value then the show will fail.
        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Unable insert shoe, Please try again.'
    # if any field is missing.
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'All fields are mandatory.'

    return HttpResponse(json.dumps(resp), content_type = "application/json")