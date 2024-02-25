from django.urls import path, include
from django.shortcuts import HttpResponse


def get_index(request):
    return HttpResponse("test")


urlpatterns: list = [
    path("", get_index)
]

