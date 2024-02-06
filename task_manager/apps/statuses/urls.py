from django.urls import path, include
from .views import StatusesView

urlpatterns = [
    path('', StatusesView.as_view(), name='statuses_list'),
]