from django.shortcuts import get_object_or_404
from todolist.models import Tasks
from django.views.generic import TemplateView


class TaskDetailView(TemplateView):
    template_name = 'task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo_task'] = get_object_or_404(Tasks, pk=kwargs['pk'])
        return context