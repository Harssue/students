from django import forms
from .models import Student

class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ("name", 'roll', 'marks')
