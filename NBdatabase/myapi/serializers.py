from rest_framework import serializers
from .models import Student
from .models import Instructor

class StudentSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta:
        model = Student
        fields = ('id', 'firstName', 'lastName', 'userId')
class InstructorSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta:
        model = Instructor
        fields = ('id', 'firstName', 'lastName', 'userId')