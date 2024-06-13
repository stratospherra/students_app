from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'middle_name', 'last_name', 'date_of_birth', 'email', 'phone', 'faculty', 'speciality', 'status']


# class StudentInline(admin.StackedInline):
#     model = Student
#     form = StudentForm
#     extra = 1
