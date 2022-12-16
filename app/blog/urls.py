from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>', views.post, name='post'),
    path('search/', views.search, name='search'),
    path('edit/', views.edit, name="edit"),
    path('comment/<int:post_id>', views.comment, name="comment"),
    path('login/', views.log_in, name="login"),
    path('logout/', views.log_out, name="logout"),
    path('signup/', views.sign_up, name="signup")
]
