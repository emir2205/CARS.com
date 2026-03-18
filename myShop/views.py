from django.shortcuts import get_object_or_404, render

from myShop.models import Category, Product


def category_list_view(request):
    if request.method == 'GET':
        categories = Category.objects.all().order_by('-id')
    return render(request, 'categories.html', {'categories': categories})


def product_list_view(request):
    if request.method == 'GET':
        products = Product.objects.all().order_by('-id')
    return render(request, 'products.html', {'products': products})


def category_products_view(request, id):
    category = get_object_or_404(Category, id=id)
    products = Product.objects.filter(category=category).order_by('-id')
    return render(
        request,
        'category_products.html',
        {'category': category, 'products': products},
    )
