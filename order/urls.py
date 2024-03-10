from django.urls import path
from . import views


urlpatterns: list = [
    path('add-favorites', views.AddFavoriteView.as_view(), name='add_favorites'),
    path('favorites', views.MyFavoritesView.as_view(), name='favorites'),
]

