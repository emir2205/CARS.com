from django.urls import path
from .views import ford_fact, xiami_fact, toyota_fact

urlpatterns = [
    path('ford/', ford_fact),
    path('xiaomi/', xiami_fact),
    path('toyota/', toyota_fact),
]
