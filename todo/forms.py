from django import forms

from todo.models import Task, Tag


class TaskForm(forms.ModelForm):
    deadline = forms.DateField(
        widget=forms.SelectDateWidget,
        required=False
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Task
        fields = "__all__"
