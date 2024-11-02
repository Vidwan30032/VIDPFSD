from django import forms
from .models import Task, StudentList, feedback


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentList
        fields = ['Register_Number','Name']

class feedbackForm(forms.ModelForm):
    class Meta:
        model = feedback
        fields = ['name', 'email', 'phonenumber', 'textfield']