from django.urls import path

from users.views import AuthLoginView, AuthLogoutView, CongView, RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', AuthLoginView.as_view(), name='login'),
    path('logout/', AuthLogoutView.as_view(), name='logout'),
    path('congratulation/', CongView.as_view(), name='congratulation'),
]
