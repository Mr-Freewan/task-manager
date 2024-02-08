from django.urls import path, include
from .views import UsersView, UserCreateView, UserUpdateView, UserDeleteView

urlpatterns = [
    path('', UsersView.as_view(), name='users_list'),
    path('create/', UserCreateView.as_view(), name='user_create'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
]


