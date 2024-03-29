'''
urlpatterns: list = [
    path('add-favorites', views.AddFavoriteView.as_view(), name='add_favorites'),
    path('favorites', views.MyFavoritesView.as_view(), name='favorites'),
]

urlpatterns.append(path("addtocart/<int:id>", views.addtocart, name="addtocart"))
urlpatterns.append(path("shopcart", views.ShopCartDetailView.as_view(), name="shopocart"))
urlpatterns.append(path("shopcart/<task>/<pk>", views.ShopCartDetailView.as_view(), name="shopocart-task"))

'''

from django.urls import path
from . import views

urlpatterns = [
    path('add-favorites', views.AddFavoriteView.as_view(), name='add_favorites'),
    path('favorites', views.MyFavoritesView.as_view(), name='favorites'),
    path("addtocart/<int:id>", views.addtocart, name="addtocart"),
    path("shopcart", views.ShopCartDetailView.as_view(), name="shopocart"),
    path("shopcart/<task>/<pk>", views.ShopCartDetailView.as_view(), name="shopocart-task"),
]
