from django.shortcuts import get_object_or_404, redirect, render

from drivers.forms import DriverForm
from drivers.models import DriverModel


def create_driver_view(request):
    if request.method == 'POST':
        form = DriverForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/driver_list/')
    else:
        form = DriverForm()
    return render(request, 'create_driver.html', {'form': form})


def driver_list_view(request):
    if request.method == 'GET':
        drivers = DriverModel.objects.all().order_by('-id')
    return render(request, 'driver_list.html', {'drivers': drivers})


def update_driver_view(request, id):
    driver_id = get_object_or_404(DriverModel, id=id)
    if request.method == 'POST':
        form = DriverForm(request.POST, request.FILES, instance=driver_id)
        if form.is_valid():
            form.save()
            return redirect('/driver_list/')
    else:
        form = DriverForm(instance=driver_id)
    return render(request, 'update_driver.html', {'form': form, 'driver_id': driver_id})


def delete_driver_view(request, id):
    driver_id = get_object_or_404(DriverModel, id=id)
    driver_id.delete()
    return redirect('/driver_list/')
