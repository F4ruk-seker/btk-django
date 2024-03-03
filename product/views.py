from django.views.generic import TemplateView, DetailView
from django.shortcuts import get_object_or_404
from .models import Category, Product


class CategoryProductListView(TemplateView):
    template_name = 'category_products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if slug := kwargs.get('slug'):
            context['product_category'] = get_object_or_404(Category, slug=slug)
            context['products'] = Product.objects.filter(category=context['product_category'])
        return context


class ProductDetailView(DetailView):
    model = Product
    lookup_url_kwarg = 'slug'
    template_name = 'product_detail.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)