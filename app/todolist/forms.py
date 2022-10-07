from todolist.models.statuses import Status
from todolist.models.types import Type
from todolist.models.tasks import Tasks
from django import forms

class TaskForm(forms.ModelForm):
    status = forms.ModelChoiceField(queryset=Status.objects.all())
    type = forms.ModelMultipleChoiceField(
        queryset=Type.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Tasks
        fields = ('summary', 'description', 'status', 'type')
