from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import School, Student, Teacher, Register, Level
from .serializers import (SchoolSerializer, StudentSerializer, 
                          TeacherSerializer, LevelSerializer,
                          RegisterSerializer)


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permissions = (AllowAny)


class StudentViewSet(viewsets.ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permissions = (AllowAny)


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permissions = (AllowAny)


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    permissions = (AllowAny)


class RegisterViewSet(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer
    permissions = (AllowAny)
