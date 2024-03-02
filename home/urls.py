from django.urls import path, include
from . import views

urlpatterns: list = [
    path("", views.HomeView.as_view(), name="home_page"),
    path("about/", views.AboutView.as_view(), name="about_page"),
    path("contact/", views.ContactView.as_view(), name="contactus_page"),
]

