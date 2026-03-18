from django.urls import path

from .views import cars_detail_view, cars_list_view

urlpatterns = [
    path("cars_list/", cars_list_view),
    path("cars_list/<int:id>/", cars_detail_view),
]