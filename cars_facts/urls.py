from django.urls import path

from cars_facts.views import CarsDetailView, CarsListView, SearchView

app_name = 'cars'

urlpatterns = [
    path('', CarsListView.as_view(), name='cars'),
    path('cars_list/', CarsListView.as_view(), name='cars_list'),
    path('cars_list/<int:id>/', CarsDetailView.as_view(), name='car_detail'),
    path('search/', SearchView.as_view(), name='search'),
]
