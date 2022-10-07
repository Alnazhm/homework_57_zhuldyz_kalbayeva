from django.shortcuts import redirect, render
from todolist.models import Tasks
from django.views.generic import TemplateView
from todolist.forms import TaskForm


class TaskAddView(TemplateView):
    template_name = 'create_task.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = TaskForm()
        context['form'] = form
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect('task_detail',pk=task.pk)
        return render(request, 'create_task.html', context={'form': form})