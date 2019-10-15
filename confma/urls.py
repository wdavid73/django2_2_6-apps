from django.urls import path
from . import views
from .views import (UserUpdateView)

app_name = 'users'

urlpatterns = [
    path('' , views.home_view , name="home"),
    
    #users
    path('users/' , views.user_view , name="users_home"),
    path('users/details/' , views.user_details_view , name="user_details"),
    path('users/create/' , views.user_create_view , name="user_create"),
    path('users/<int:id>/update/' , UserUpdateView.as_view() , name="user_update"),
    path('users/<int:id>/delete/' , views.user_delete_view, name="user_delete")
    
]
