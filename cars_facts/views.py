from django.shortcuts import get_object_or_404, render

from .models import Car


def cars_list_view(request):
    cars = Car.objects.all().order_by("-id")
    return render(request, "car_list.html", {"cars": cars})


def cars_detail_view(request, id):
    car = get_object_or_404(Car, id=id)
    return render(request, "car_detail.html", {"car": car})
