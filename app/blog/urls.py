from os import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>', views.post, name='post'),
    path('search/', views.search, name='search'),
    path('edit/', views.edit, name="edit"),
    path('login/', views.login, name="login"),
    path('signup/', views.sign_up, name="signup")
]
