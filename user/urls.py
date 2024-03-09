from django.urls import path
from . import views


urlpatterns: list = [
    # path('login', views, name='user_login')
    path('logout', views.LogoutView.as_view(), name='user_logout')
    # path('register', views, name='user_register')
]

