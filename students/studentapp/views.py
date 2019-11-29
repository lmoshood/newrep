from django.shortcuts import render
from django.http import HttpResponse
from studentapp.models import Student
# Create your views here.

def home(request):
    return HttpResponse('Welcome to Home page')

def about(request):
    return HttpResponse('Welcome to about us page')


def students_list(request):
    students = Student.objects.all()
    return render(request, 'student.html', {'object_list': students})
