from django.urls import path

from myShop.views import category_list_view, category_products_view, product_list_view

urlpatterns = [
    path('categories/', category_list_view),
    path('products/', product_list_view),
    path('categories/<int:id>/', category_products_view),
]
