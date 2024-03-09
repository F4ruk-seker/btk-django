from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, DetailView, RedirectView
from django.shortcuts import get_object_or_404
from .models import Category, Product, Comment
from product.forms import CommentForm


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
        context = super().get_context_data(**kwargs)
        if product := context.get('product', None):
            context['comments'] = Comment.objects.filter(product=product)
        return context


class AddCommentView(RedirectView):
    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, id=kwargs.get('id'))
        form = CommentForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            comment = form.save(commit=False)
            comment.product = product
            comment.user_id = request.user.id
            comment.ip = request.META.get('REMOTE_ADDR')
            comment.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
