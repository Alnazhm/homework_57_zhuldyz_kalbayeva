from django.urls import path
from todolist.views.base import IndexView
from todolist.views.add_task_view import TaskAddView
from todolist.views.edit_task_view import TaskEditView
from todolist.views.delete_task_view import TaskDeleteView
from todolist.views.task_detail_view import TaskDetailView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('tasks/add/', TaskAddView.as_view(), name='task_add'),
    path('tasks/<int:pk>', TaskDetailView.as_view(), name='task_detail'),
    path('tasks/edit/<int:pk>', TaskEditView.as_view(), name='edit_task'),
    path('tasks/deleted/<int:pk>', TaskDeleteView.as_view(), name='confirm_delete')
]