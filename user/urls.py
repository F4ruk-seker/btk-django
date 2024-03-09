from django.urls import path
from . import views


auth_patterns: list = [
    path('login', views.LoginView.as_view(), name='user_login'),
    path('logout', views.LogoutView.as_view(), name='user_logout'),
    path('register', views.RegisterView.as_view(), name='user_register')
]


urlpatterns: list = [
    path('', views.PanelView.as_view(), name='panel'),
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('comments', views.UserCommentsView.as_view(), name='comments'),
    path('comment/delete', views.CommentDeleteView.as_view(), name='delete_comment'),
]
urlpatterns += auth_patterns


