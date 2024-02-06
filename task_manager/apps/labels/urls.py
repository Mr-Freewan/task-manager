from django.urls import path, include
from .views import LabelsView

urlpatterns = [
    path('', LabelsView.as_view(), name='labels_list'),
]