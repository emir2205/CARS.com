from django.core.paginator import Paginator
from django.db.models import F
from django.shortcuts import get_object_or_404, render

from cars_facts.models import Car


# поиск
def search_view(request):
    query = request.GET.get('s', '')
    if query:
        cars = Car.objects.filter(title__icontains=query)
    else:
        cars = Car.objects.none()

    return render(
        request,
        'car_list.html',
        {
            'cars_key': cars,
            'search_query': query,
        }
    )


def cars_list_view(request):
    if request.method == 'GET':
        cars = Car.objects.all().order_by('-id')
        paginator = Paginator(cars, 2)
        page = request.GET.get('page')
        page_obj = paginator.get_page(page)

        return render(
            request,
            'car_list.html',
            {
                'cars_key': page_obj,
                'search_query': '',
            }
        )


def cars_detail_view(request, id):
    if request.method == 'GET':
        car_id = get_object_or_404(Car, id=id)
        views_car = request.session.get('viewed_car', [])

        if id not in views_car:
            car_id.views = F('views') + 1
            car_id.save()
            car_id.refresh_from_db()

            views_car.append(id)
            request.session['viewed_car'] = views_car

        return render(
            request,
            'car_detail.html',
            {
                'car': car_id,
            }
        )
