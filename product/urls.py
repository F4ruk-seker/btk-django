from django.urls import path
from . import views


urlpatterns: list = [
    # path("<slug>/", views.CategoryProductListView.as_view(), name="category-product-list")
    path("product/<slug>/", views.ProductDetailView.as_view(), name="product-detail"),
    path("category/<slug>/", views.CategoryProductListView.as_view(), name="category-product-list")
]

