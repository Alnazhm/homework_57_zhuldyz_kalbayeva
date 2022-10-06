from todolist.models import Tasks
from django.views.generic.edit import DeleteView


class TaskDeleteView(DeleteView):
    model = Tasks
    success_url = '/'
    template_name = 'delete_confirm_page.html'