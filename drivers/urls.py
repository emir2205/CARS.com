from django.urls import path

from drivers.views import (
    CreateDriverView,
    DeleteDriverView,
    DriverListView,
    UpdateDriverView,
)

urlpatterns = [
    path('create_driver/', CreateDriverView.as_view()),
    path('driver_list/', DriverListView.as_view()),
    path('driver_list/<int:id>/', UpdateDriverView.as_view()),
    path('driver_list/<int:id>/delete/', DeleteDriverView.as_view()),
]
