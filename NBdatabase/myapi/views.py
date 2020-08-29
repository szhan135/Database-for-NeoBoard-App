from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StudentSerializer
from .serializers import InstructorSerializer
from .models import Student
from .models import Instructor

# Create your views here.
class StudentViewSet(viewsets.ModelViewSet) :
    queryset = Student.objects.all().order_by('id')
    serializer_class = StudentSerializer
class InstructorViewSet(viewsets.ModelViewSet) :
    queryset = Instructor.objects.all().order_by('id')
    serializer_class = InstructorSerializer