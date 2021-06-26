from django.urls import path
from .views import AllTasks, CreateTask, EditTask, DeleteTask, DetailTask

urlpatterns = [
    path('', AllTasks.as_view(), name='all-tasks'),
    path('create-task/', CreateTask.as_view(), name='create-task'),
    path('edit-task/<int:pk>/', EditTask.as_view(), name='edit-task'),
    path('delete-task/<int:pk>/', DeleteTask.as_view(), name='delete-task'),
    path('detail-task/<int:pk>', DetailTask.as_view(), name='detail-task'),
]