from django.urls import path
from todolist.views.base import IndexView, TaskAddView, TaskDetailView, TaskDeleteView, TaskEditView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('tasks/add/', TaskAddView.as_view(), name='task_add'),
    path('tasks/<int:pk>', TaskDetailView.as_view(), name='task_detail'),
    path('tasks/edit/<int:pk>', TaskEditView.as_view(), name='edit_task'),
    path('tasks/deleted/<int:pk>', TaskDeleteView.as_view(), name='confirm_delete')
]