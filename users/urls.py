from django.urls import path

from users import views

urlpatterns = [
    path('register/', views.register_view),
    path('login/', views.auth_view),
    path('logout/', views.logout_view),
    path('congratulation/', views.cong_view),
]
