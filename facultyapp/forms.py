from .models import AddCourse
from django import forms

class AddCourseForm(forms.ModelForm):
    class Meta:
        model = AddCourse
        fields = ['student','course','section']

