from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import RedirectView, ListView

from order.models import Favorite


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

