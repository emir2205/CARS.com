from django.views import generic

from myShop.models import Category, Product


class CategoryListView(generic.ListView):
    template_name = 'categories.html'
    model = Category
    context_object_name = 'categories'

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


class ProductListView(generic.ListView):
    template_name = 'products.html'
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


class CategoryProductsView(generic.DetailView):
    template_name = 'category_products.html'
    model = Category
    context_object_name = 'category'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(category=context['category']).order_by('-id')
        return context
