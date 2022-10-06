from django.shortcuts import get_object_or_404, redirect, render
from todolist.models import Tasks
from django.views.generic import TemplateView
from todolist.forms import TaskForm
from django.views.generic.edit import DeleteView


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo_tasks'] = Tasks.objects.all()
        return context


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
            task = Tasks.objects.create(**form.cleaned_data)
            return redirect('task_detail',pk=task.pk)
        return render(request,'create_task.html',context={'form':form})


class TaskDetailView(TemplateView):
    template_name = 'task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo_task'] = get_object_or_404(Tasks, pk=kwargs['pk'])
        return context


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


class TaskDeleteView(DeleteView):
    model = Tasks
    success_url = '/'
    template_name = 'delete_confirm_page.html'
