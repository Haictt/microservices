from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json

from django.views.decorators.csrf import csrf_exempt
from clothe_model.models import clothe_model

@csrf_exempt
def get_clothes(request):
    data = []
    resp = {}

    prod_data = clothe_model.objects.all()

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

def data_insert(product_category, clothe_name, availability, price,color):
    clothe_data = clothe_model(
        product_category = product_category,
        clothe_name = clothe_name,
        availability = availability,
        price = price,
        color = color
    )

    clothe_data.save()
    return 1

@csrf_exempt
# get the data from the front end.
def insertClothe_req(request):
    product_category = request.POST.get("Product category")
    clothe_name = request.POST.get("Clothe name")
    availability = request.POST.get("Availability")
    price = request.POST.get("Price")
    color = request.POST.get("Color")
    resp = {}

    # checking that all fields are available.
    if product_category and clothe_name and availability and price and color:
        respdata = data_insert(product_category, clothe_name, availability, price,color)

        # if it returns value then will show success.
        if respdata:
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['message'] = 'Clothe is insert Successfully.'
        # else returning any value then the show will fail.
        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Unable insert clothe, Please try again.'
    # if any field is missing.
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'All fields are mandatory.'

    return HttpResponse(json.dumps(resp), content_type = "application/json")