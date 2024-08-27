from carmarket.models import Car, Brand, Order
from django.shortcuts import render,redirect


def home(request):
    brands = Brand.objects.all()
    cars = Car.objects.all()
    selected_brand = request.GET.get('brand')
    if selected_brand:
        cars = cars.filter(brand__name=selected_brand)
    else:
        cars = Car.objects.all()
    return render(request, 'home.html', {'brands': brands, 'cars': cars, 'selected_brand': selected_brand})
