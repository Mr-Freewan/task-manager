from django.urls import path, include
from .views import UsersView, UserCreateView

urlpatterns = [
    path('', UsersView.as_view(), name='users_list'),
    path('create/', UserCreateView.as_view(), name='user_create'),
]
