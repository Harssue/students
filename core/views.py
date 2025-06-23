from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from .models import Student
from .forms import AddStudentForm
from rest_framework import viewsets
from .serializers import StudentSerializer
# Create your views here.

def home_view(request):
    students = Student.objects.all()
    return render(request, 'core/home.html', {'stu_data':students})

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class AddStudent(View):
    def get(self, request):
        fm = AddStudentForm()
        return render(request, 'core/add-student.html', {'form':fm})
    
    def post(self, request):
        fm = AddStudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/home')
        else:
            return render(request, 'core/add-student.html', {'form':fm})
    
class DeleteStudent(View):
    def post(self, request):
        data = request.POST
        id = data.get('id')
        studata = Student.objects.get(id=id)
        studata.delete()
        return redirect('/home')

class EditStudent(View):
    def get(self, request, id):
        student = Student.objects.get(pk=id)
        form = AddStudentForm(instance=student)
        return render(request, 'core/edit-student.html', {'form':form})
    
    def post(self, request, id):
        student = Student.objects.get(pk=id)
        form = AddStudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/home')
        return render(request, 'core/edit-student.html', {'form':form})