from django.shortcuts import get_object_or_404, redirect
from django.views import generic

from drivers.forms import DriverForm
from drivers.models import DriverModel


class CreateDriverView(generic.CreateView):
    template_name = 'create_driver.html'
    form_class = DriverForm
    success_url = '/driver_list/'


class DriverListView(generic.ListView):
    template_name = 'driver_list.html'
    model = DriverModel
    context_object_name = 'drivers'

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


class UpdateDriverView(generic.UpdateView):
    template_name = 'update_driver.html'
    form_class = DriverForm
    model = DriverModel
    success_url = '/driver_list/'

    def get_object(self, **kwargs):
        driver_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=driver_id)


class DeleteDriverView(generic.View):
    def get(self, request, id):
        driver_id = get_object_or_404(DriverModel, id=id)
        driver_id.delete()
        return redirect('/driver_list/')
