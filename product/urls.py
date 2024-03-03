from django.urls import path
from . import views


urlpatterns: list = [
    # path("<slug>/", views.CategoryProductListView.as_view(), name="category-product-list")
    path("<slug>/", views.CategoryProductListView.as_view(), name="category-product-list")
]

