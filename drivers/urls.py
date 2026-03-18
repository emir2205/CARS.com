from django.urls import path

from drivers.views import (
    create_driver_view,
    delete_driver_view,
    driver_list_view,
    update_driver_view,
)

urlpatterns = [
    path('create_driver/', create_driver_view),
    path('driver_list/', driver_list_view),
    path('driver_list/<int:id>/', update_driver_view),
    path('driver_list/<int:id>/delete/', delete_driver_view),
]
