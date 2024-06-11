from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from .forms import StudentForm

def index(request):
    return render(request, 'index.html')

def student_profile(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'student_profile.html', {'student': student})

def edit_student_profile(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_profile', student_id=student.id)
    else:
        form = StudentForm(instance=student)
    return render(request, 'edit_student_profile.html', {'form': form})
