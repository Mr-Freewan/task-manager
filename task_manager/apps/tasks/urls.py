from django.urls import path

from .views import TasksView, TaskCreateView, TaskUpdateView, TaskDeleteView, \
    TaskInfoView

urlpatterns = [
    path('', TasksView.as_view(), name='tasks_list'),
    path('<int:pk>/', TaskInfoView.as_view(), name='task_info'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
]
