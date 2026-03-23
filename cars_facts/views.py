from django.db.models import F
from django.views import generic

from cars_facts.models import Car


class SearchView(generic.ListView):
    template_name = 'car_list.html'
    context_object_name = 'cars_key'
    model = Car

    def get_queryset(self):
        query = self.request.GET.get('s', '')
        if query:
            return self.model.objects.filter(title__icontains=query)
        return self.model.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('s', '')
        return context


class CarsListView(generic.ListView):
    template_name = 'car_list.html'
    model = Car
    context_object_name = 'cars_key'
    paginate_by = 2

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cars_key'] = context['page_obj']
        context['search_query'] = ''
        return context


class CarsDetailView(generic.DetailView):
    template_name = 'car_detail.html'
    context_object_name = 'car'
    pk_url_kwarg = 'id'
    model = Car

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        request = self.request

        viewed_car = request.session.get('viewed_car', [])

        if obj.pk not in viewed_car:
            Car.objects.filter(pk=obj.pk).update(views=F('views') + 1)
            viewed_car.append(obj.pk)
            request.session['viewed_car'] = viewed_car
            obj.refresh_from_db()

        return obj
