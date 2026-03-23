from django.urls import path

from cars_facts.views import cars_detail_view, cars_list_view, search_view

app_name = 'cars'

urlpatterns = [
    path('', cars_list_view, name='cars'),
    path('cars_list/<int:id>/', cars_detail_view, name='car_detail'),
    path('search/', search_view, name='search'),
]
