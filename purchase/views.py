from django.shortcuts import render, redirect
from car.models import CarModel
from car.forms import CarForm
from purchase.models import PurchaseClass
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def purchase(request, id, count__gt=0):
    car_obj = CarModel.objects.get(pk=id)
    if car_obj is None:
        messages.error(request, 'Car not found or no quantity available.')
        return redirect('home')
    else:
        car_obj.quantity -= 1
        car_obj.save()
        PurchaseClass.objects.create(user=request.user, car=car_obj)
        messages.success(request, 'Car purchased successfully.')
        purchase_obj = PurchaseClass.objects.filter(user=request.user.id)
        return render(request, 'profile.html', {'cars':purchase_obj})