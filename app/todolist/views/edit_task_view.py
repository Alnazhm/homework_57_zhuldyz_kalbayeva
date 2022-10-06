from django.shortcuts import redirect, render, get_object_or_404
from todolist.models import Tasks
from django.views.generic import TemplateView
from todolist.forms import TaskForm

class TaskEditView(TemplateView):
    template_name = 'task_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo_task'] = get_object_or_404(Tasks, pk=kwargs['pk'])
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = TaskForm(instance=context['todo_task'])
        context['form'] = form
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        todo_task = get_object_or_404(Tasks, pk=kwargs['pk'])
        form = TaskForm(request.POST, instance=todo_task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', pk=todo_task.pk)
        return render(request, 'task_edit.html', context={'form': form})