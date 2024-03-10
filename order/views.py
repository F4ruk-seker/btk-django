from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import RedirectView, ListView, DetailView, UpdateView, DeleteView, TemplateView
from product.models import Product
from order.models import Favorite, ShopCart
from order.forms import OrderForm, ShopCartForm


class AddFavoriteView(LoginRequiredMixin, RedirectView):
    def post(self, request, *args, **kwargs):
        queryset = {
            'user': request.user,
            'product_id': request.POST.get('product_id')
        }
        if favorite := Favorite.objects.filter(**queryset).first():
            favorite.delete()
        else:
            Favorite.objects.create(**queryset)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class MyFavoritesView(LoginRequiredMixin, ListView):
    model = Favorite
    template_name = 'all_favorites.html'
    context_object_name = 'favorites'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

@login_required(login_url='/login')  # Check login
def delfavorite(request,id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    Favorite.objects.filter(product_id=id, user_id=current_user.id).delete()
    return HttpResponseRedirect(url)

@login_required(login_url='/login')  # Check login
def addtocart(request, id):
    url = request.META.get('HTTP_REFERER')  # get last url
    current_user = request.user  # Access User Session information
    product = Product.objects.get(pk=id)

    checkinproduct = ShopCart.objects.filter(product_id=id, user_id=current_user.id)  # Check product in shopcart
    if checkinproduct:
        control = 1  # The product is in the cart
    else:
        control = 0  # The product is not in the cart"""

    if request.method == 'POST':  # if there is a post
        form = ShopCartForm(request.POST)
        if form.is_valid():
            if control == 1:  # Update  shopcart
                data = ShopCart.objects.get(product_id=id, user_id=current_user.id)
                data.quantity += form.cleaned_data['quantity']
                data.save()  # save data
            else:  # Inser to Shopcart
                data = ShopCart()
                data.user_id = current_user.id
                data.product_id = id
                data.quantity = form.cleaned_data['quantity']
                data.save()
        messages.success(request, "Product added to Shopcart ")
        request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()
        return HttpResponseRedirect(url)

    else:  # if there is no post
        if control == 1:  # Update  shopcart
            data = ShopCart.objects.get(product_id=id, user_id=current_user.id)
            data.quantity += 1
            data.save()  #
        else:  # Inser to Shopcart
            data = ShopCart()  # model ile bağlantı kur
            data.user_id = current_user.id
            data.product_id = id
            data.quantity = 1
            data.save()  #
        request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()
        messages.success(request, "Product added to Shopcart")
        return HttpResponseRedirect(url)

def shopcart(request):
    current_user = request.user  # Access User Session information
    total: float = 0.
    if shop_cart := ShopCart.objects.filter(user_id=current_user.id):
        total = sum([_.amount for _ in shop_cart])
    context = {'shopcart': shop_cart,
               'total': total,
               }
    return render(request, 'shopcart_products.html', context)


class ShopCartDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'shopcart_products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shopcart'] = ShopCart.objects.filter(user=self.request.user)
        context['total'] = 0
        if context['shopcart']:
            context['total'] = sum([_.amount for _ in context['shopcart']])
        return context

    def post(self, request, *args, **kwargs):
        if (task := request.POST.get('task')) and (product := request.POST.get('product')):
            match task:
                case 'delete':
                    shop_cart = get_object_or_404(ShopCart, product_id=product, user=self.request.user)
                    shop_cart.delete()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

