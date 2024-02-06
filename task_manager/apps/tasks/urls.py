from django.urls import path, include
from .views import TasksView

urlpatterns = [
    path('', TasksView.as_view(), name='tasks_list'),
]