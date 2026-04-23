from django.shortcuts import render, get_object_or_404
from .models import Brand, Car

def home(request):
    return render(request, 'main/index.html', {
        'brands': Brand.objects.all(),
        'cars': Car.objects.all().select_related('brand')
    })

def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    return render(request, 'main/detail.html', {'car': car})