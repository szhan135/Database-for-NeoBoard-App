from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StudentSerializer
from .models import Student

# Create your views here.
class StudentViewSet(viewsets.ModelViewSet) :
    queryset = Student.objects.all().order_by('id')
    serializer_class = StudentSerializer