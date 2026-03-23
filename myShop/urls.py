from django.urls import path

from myShop.views import CategoryListView, CategoryProductsView, ProductListView

urlpatterns = [
    path('categories/', CategoryListView.as_view()),
    path('products/', ProductListView.as_view()),
    path('categories/<int:id>/', CategoryProductsView.as_view()),
]
