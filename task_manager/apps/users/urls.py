from django.urls import path, include
from .views import UsersView

urlpatterns = [
    path('', UsersView.as_view(), name='users_list'),
]