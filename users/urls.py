from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', UserListView.as_view(), name='users_list'),
    path('create/', UserCreateView.as_view(), name='users_create'),
    # path('index/', index, name='index'),
    path('index/', Index.as_view(), name='index'),
    # path('create_user/', create_user, name='create_user'),
    path('create_user/', CreateUser.as_view(), name='create_user'),

]
