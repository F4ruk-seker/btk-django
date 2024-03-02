from django.urls import path, include
from .views import HomeView

urlpatterns: list = [
    path("", HomeView.as_view(), name="")
]

