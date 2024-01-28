from django.shortcuts import render
from car.models import CarModel
from brand.models import BrandModel


def home(request, brand_slug=None):
    carobj = CarModel.objects.all()
    if brand_slug is not None:
        braObj = BrandModel.objects.get(slug=brand_slug)
        carobj = CarModel.objects.filter(brand=braObj)
    braObj = BrandModel.objects.all()
    return render(request, 'home.html', {'data':carobj, 'data2' : braObj})

